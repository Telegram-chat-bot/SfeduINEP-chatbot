import logging

from loader import dp, bot
from aiogram.types import Message

from aiogram.dispatcher import FSMContext
from states.state_machine import User_State, PositionState, Questions

from utils.db_api.db_commands import get_faq, get_chat_id_group_directions, get_chat_id_admission

from datetime import datetime

from keyboards.inline import buttons as btn


# РАЗДЕЛ ЗАДАТЬ ВОПРОС
@dp.message_handler(text="F.A.Q")
async def answers(message: Message):
    await message.answer(await get_faq())


# Обработчик по нажатию на кнопку Вопросы по поступлению
@dp.message_handler(text="Вопросы по поступлению")
async def admission_questions(message: Message):
    await message.answer(
        "Задайте свой вопрос в диалоге. Он будет направлен представителю приёмной комиссии, который ответит Вам, "
        "как только сможет")
    await Questions.question.set()


# Обработчтк по нажатиию на кнопку по направлению
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


# -----------------------------------


# СТЭЙТЫ-----------------------------
# Формирование вопроса по поступлению
@dp.message_handler(state=Questions.question)
async def question_handler(message: Message, state: FSMContext):
    chat_id_group = await get_chat_id_admission()

    try:
        await bot.send_message(chat_id=chat_id_group, text=f"""
{datetime.now().strftime("%d.%m.%Y %H:%M")}
Вопрос от <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name} {message.from_user.last_name}</a>
Его id {message.from_user.id}
    
    "{message.text}"
        """
                               )
        await message.answer("Ваш вопрос был учитан и отправлен приёмной комиссии. Ожидайте ответа")
    except Exception:
        await message.answer("Произошла ошибка")

    await state.finish()


@dp.message_handler(state=Questions.user_question_dir)
async def handler(message: Message, state: FSMContext):
    question = message.text

    await state.set_state(User_State.direction)

    try:
        direction = await state.get_data()

        choosed_direction = direction.get("direction")
        chat_id = await get_chat_id_group_directions(choosed_direction)

        await bot.send_message(chat_id=chat_id, text=f"""
{datetime.now().strftime("%d.%m.%Y %H:%M")}
Вопрос от <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name} {message.from_user.last_name}</a> по направлению {choosed_direction}
Его id: <b>{message.from_user.id}</b>

"{question}"
"""
                               )
        await message.answer("Ваш вопрос был учитан и отправлен руководителю направления. Ожидайте ответа")
    except:
        await message.answer(f"Группа по этому направлению еще не создана или не занесена в базу данных")

    await state.finish()
