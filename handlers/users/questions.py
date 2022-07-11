import logging
from loader import dp, bot
from utils.debugger import debugger
from filters import IsNotButton
from datetime import datetime

from states.state_machine import PositionState, Questions, UserState, Feedback

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from django_admin.bot.models import InnerKeyboard
from django_admin.service.models import ChatIDAdmission

from handlers.users.main_menu import inner_buttons_id, buttons_id, buttons_title_second
from keyboards.inline.buttons import choose_level

from keyboards.inline import group_buttons as group_btn

from utils.db_api.db_commands import get_chat_id_group_directions, Database
from django_admin.feedback.models import Feedback as FB_Model
from keyboards.default import enrollee_menu as kb


@dp.message_handler(text="Вопросы по направлению подготовки")
async def direction_training_questions(message: Message, state: FSMContext):
    pressed_button: str = message.text
    btn_id: int = inner_buttons_id[pressed_button]

    comment: tuple = InnerKeyboard.objects.filter(
        btn_title=pressed_button,
        buttons_id=btn_id
    ).values_list("info").last()

    await message.answer(
        *comment,
        reply_markup=choose_level)

    await state.set_state(PositionState.set_pressed_btn)
    async with state.proxy() as data:
        data["page"] = "question_for_dir"

    await PositionState.next()


# * Формирование вопроса по направлению подготовки
@dp.message_handler(IsNotButton([*inner_buttons_id.keys(), *buttons_id.keys(), "Назад"]), state=Questions.user_question_dir)
async def handler(message: Message, state: FSMContext):
    question: str = message.text
    await state.set_state(UserState.direction)

    # Формирование кнопки для ответа, которая прикрепляется к сообщению с вопросом в группе
    button: InlineKeyboardMarkup = await group_btn.gen_answer_btn(user_id=message.from_user.id)

    try:
        direction_data: dict = await state.get_data()
        chosen_direction: str = direction_data.get("direction")

        chat_id = await get_chat_id_group_directions(chosen_direction)
        await bot.send_message(
            chat_id=chat_id, text=f"""{datetime.now().strftime("%d.%m.%Y %H:%M")}
Вопрос от \
<a href='tg://user?id={message.from_user.id}'>\
{message.from_user.first_name or message.from_user.username} {message.from_user.last_name or ''}\
</a> по направлению {chosen_direction}

"{question}"
""", reply_markup=button
            )

        await message.answer("Ваш вопрос учтён и отправлен руководителю направления. Ожидайте ответа")

    except ObjectDoesNotExist as error:
        await message.answer("Группа по этому направлению еще не создана или не занесена в базу данных")
        logging.error(error)

    await state.finish()


# * Обработчик нажатия кнопки Вопросы по поступлению
@dp.message_handler(text="Вопросы по поступлению")
async def admission_questions(message: Message):
    pressed_button: str = message.text
    information: str = InnerKeyboard.objects.get(
        btn_title=pressed_button
    ).info

    await message.answer(information)
    await Questions.user_question.set()


# * Формирование вопроса по поступлению
@dp.message_handler(IsNotButton([*inner_buttons_id.keys(), *buttons_id.keys(), "Назад"]), state=Questions.user_question)
async def question_handler(message: Message, state: FSMContext):
    try:
        question: str = message.text
        chat_id_group: str = await Database(ChatIDAdmission).get_field_by_name("chat_id")

        button = await group_btn.gen_answer_btn(user_id=message.from_user.id)

        await bot.send_message(
            chat_id=chat_id_group,
            text=f"""{datetime.now().strftime("%d.%m.%Y %H:%M")}
Вопрос от <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name} {message.from_user.last_name}</a>

"{question}" """, reply_markup=button
                        )

        await message.answer("Ваш вопрос учтён и отправлен приёмной комиссии. Ожидайте ответа")

    except MultipleObjectsReturned as error:
        await message.answer(f"Ошибка 500. Не удалось отправить сообщение\n{await debugger(str(error))}")

    except ObjectDoesNotExist as error:
        await message.answer(f"Ошибка! Группы, куда должен быть направлен вопрос, не существует.\n{await debugger(str(error))}")
        logging.error(error)

    await state.finish()


# * Обработчик кнопки Обратная связь
@dp.message_handler(text="Обратная связь")
async def feedback_page(message: Message):
    pressed_button: str = message.text
    btn_id: int = inner_buttons_id[pressed_button]

    comment: tuple = InnerKeyboard.objects.filter(
        btn_title=pressed_button,
        buttons_id=btn_id
    ).values_list("info").last()

    await message.answer(*comment)

    await Feedback.feedback_message.set()


# * Формирование отзыва пользователя и отправка его на сервер
@dp.message_handler(state=Feedback.feedback_message)
async def get_feedback(message: Message, state: FSMContext):
    if message.text in buttons_title_second or message.text in ["Обратная связь", "Назад"]:
        await message.answer("Введите свой отзыв или активируйте команду /exit для выхода из режима ожидания ввода")
    else:
        fb_message: str = message.text
        user_name: str = ' '.join(
            [
                message.from_user.first_name or "", message.from_user.last_name or ""
            ]
        )

        await Database(FB_Model).save_data(username=user_name, review=fb_message)
        await message.answer("Ваш отзыв отправлен!", reply_markup=await kb.generate_keyboard(one_time_keyboard=True))

        await state.finish()
