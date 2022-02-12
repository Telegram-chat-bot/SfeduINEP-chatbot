import logging

from loader import dp, bot
from aiogram.types import Message

from aiogram.dispatcher import FSMContext
from states.state_machine import UserState, PositionState, Questions, Feedback
from utils.db_api import db_commands

from utils.db_api.db_commands import get_faq, get_chat_id_group_directions, get_chat_id_admission

from datetime import datetime

from keyboards.default import enrollee_menu as kb
from keyboards.inline import buttons as btn
from keyboards.inline import group_buttons as group_btn

buttons = [
    "Назад",
    "F.A.Q",
    "Обратная связь",
    "Вопросы по поступлению",
    "Вопросы по направлению подготовки"
]


# РАЗДЕЛ ЗАДАТЬ ВОПРОС
@dp.message_handler(text="F.A.Q")
async def answers(message: Message):
    await message.answer(await get_faq())


# Обработчик нажатия кнопки Вопросы по поступлению
@dp.message_handler(text="Вопросы по поступлению")
async def admission_questions(message: Message):
    await message.answer(
        "Задайте свой вопрос в диалоге. Он будет направлен представителю приёмной комиссии, который ответит Вам, "
        "как только сможет")
    await Questions.user_question.set()


# Формирование вопроса по поступлению
@dp.message_handler(state=Questions.user_question)
async def question_handler(message: Message, state: FSMContext):
    if message.text not in buttons:  # если не была нажата кнопка из клавиатуры после нажатия на кнопку с вопросом
        question = message.text
        chat_id_group = await get_chat_id_admission()

        button = await group_btn.gen_answer_btn(user_id=message.from_user.id)
        try:
            await bot.send_message(chat_id=chat_id_group, text=f"""
{datetime.now().strftime("%d.%m.%Y %H:%M")}
Вопрос от <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name} {message.from_user.last_name}</a>

"{question}"
            """, reply_markup=button
                                   )

            await message.answer("Ваш вопрос учтён и отправлен приёмной комиссии. Ожидайте ответа")
        except Exception as error:
            await message.answer("Произошла ошибка")
            logging.error(error)

        await state.finish()

    else:
        await message.answer("Выход из режима ввода текста")
        await state.finish()


# Обработчик  нажатиия кнопки вопроса по направлению
@dp.message_handler(text="Вопросы по направлению подготовки")
async def direction_training_questions(message: Message, state: FSMContext):
    await message.answer(
        "Задайте свой вопрос в диалоге. Он будет направлен руководителю направления подготовки, который ответит Вам, "
        "как только сможет",
        reply_markup=btn.choose_level)

    await state.set_state(PositionState.set_pressed_btn)
    async with state.proxy() as data:
        data["page"] = "question_for_dir"

    await PositionState.next()


@dp.message_handler(text="Обратная связь")
async def feedback_page(message: Message):
    await message.answer(
        """Здесь вы можете выразить свое мнение по поводу текущего тех. состояния чат-бота или предложить свои идеи по его улучшению.
        
Мы <ins>всегда</ins> открыты для критики и сделаем всё возможное, чтобы пользование ботом для <b>Вас</b> было наиболее комфортным.
"""
    )
    await Feedback.feedback_message.set()


# Формирование отзыва пользователя и отправка его на сервер
@dp.message_handler(state=Feedback.feedback_message)
async def get_feedback(message: Message, state: FSMContext):
    if message.text not in buttons:
        fb_message = message.text
        user_name = ' '.join(
            [
                message.from_user.first_name or "", message.from_user.last_name or ""
            ]
        )
        await db_commands.send_feedback(username=user_name, review=fb_message)
        await message.answer("Ваш отзыв отправлен!", reply_markup=kb.main_menu)

        await state.finish()
    else:
        await message.answer("Выход из режима ввода текста")
        await state.finish()


# Формирование вопроса по направлению подготовки
@dp.message_handler(state=Questions.user_question_dir)
async def handler(message: Message, state: FSMContext):
    if message.text not in buttons:
        question = message.text

        await state.set_state(UserState.direction)

        # Формирование кнопки для ответа, которая прикрепляется к сообщению с вопросом в группе
        button = await group_btn.gen_answer_btn(user_id=message.from_user.id)
        try:
            direction = await state.get_data()

            chosen_direction = direction.get("direction")
            chat_id = await get_chat_id_group_directions(chosen_direction)

            await bot.send_message(chat_id=chat_id, text=f"""
{datetime.now().strftime("%d.%m.%Y %H:%M")}
Вопрос от <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name or message.from_user.username} {message.from_user.last_name or ''}</a> по направлению {chosen_direction}

"{question}"
""", reply_markup=button
                                   )
            await message.answer("Ваш вопрос учтён и отправлен руководителю направления. Ожидайте ответа")

        except Exception as error:
            await message.answer(f"Группа по этому направлению еще не создана или не занесена в базу данных")
            logging.error(error)

        await state.finish()

    else:
        await message.answer("Выход из режима ввода")
        await state.finish()
