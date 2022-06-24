from datetime import datetime

import aiofiles

import os
from django_admin.django_admin.settings import MEDIA_ROOT

from aiogram.dispatcher.storage import FSMContext

from aiogram.utils.exceptions import MessageTextIsEmpty, CantParseEntities
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from django_admin.bot.models import Page, InfoPage, InnerKeyboard
from django_admin.service.models import ChatIDAdmission
from django_admin.feedback.models import Feedback as FB_Model

from filters import CommandBack
from keyboards.inline.buttons import choose_level

from states.state_machine import PositionState, Feedback, Questions, UserState
from loader import dp, bot, debug
from aiogram.types import Message

from keyboards.default import enrollee_menu as kb
from keyboards.inline import group_buttons as group_btn

import logging

from utils import google_sheets
from utils.db_api import db_commands
from utils.db_api.db_commands import Database, get_chat_id_group_directions

# * Формирование словаря кнопок первого уровня => кнопка : id
buttons = Page.objects.values("btn_title", "id")
buttons_id: dict = {}
for btn in buttons:
    buttons_id[btn['btn_title']] = btn["id"]

# * Формирование словаря кнопок второго уровня => кнопка : id
inner_buttons = InnerKeyboard.objects.values("btn_title", "buttons_id")
inner_buttons_id: dict = {}
for btn in inner_buttons:
    inner_buttons_id[btn["btn_title"]] = btn["buttons_id"]

# * Формирование списка кнопок
buttons_title_first = []
buttons_title_second = []
keyboard = {}
for btn in buttons_id:
    buttons_title_first.append(btn)
keyboard["first"] = buttons_title_first

for btn in inner_buttons_id:
    buttons_title_second.append(btn)
keyboard["second"] = buttons_title_second


# * Обработчик кнопки Назад
@dp.message_handler(CommandBack())
async def back_to_btn_handler(message: Message):
    await message.answer("Вы вернулись назад", reply_markup=kb.generate_keyboard(
        one_time_keyboard=True
    ))


# * Обработчик  нажатиия кнопки вопроса по направлению
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
@dp.message_handler(state=Questions.user_question_dir)
async def handler(message: Message, state: FSMContext):
    if message.text not in (inner_buttons_id and buttons_id) and message.text != "Назад":
        question: str = message.text

        await state.set_state(UserState.direction)

        # Формирование кнопки для ответа, которая прикрепляется к сообщению с вопросом в группе
        button = await group_btn.gen_answer_btn(user_id=message.from_user.id)
        try:
            direction = await state.get_data()

            chosen_direction: str = direction.get("direction")

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
            await message.answer(f"Группа по этому направлению еще не создана или не занесена в базу данных")
            logging.error(error)

        await state.finish()

    else:
        await message.answer("Выход из режима ввода")
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
        await message.answer("Ваш отзыв отправлен!", reply_markup=kb.generate_keyboard(one_time_keyboard=True))

        await state.finish()


#  РАЗДЕЛ ЗАДАТЬ ВОПРОС
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
@dp.message_handler(state=Questions.user_question)
async def question_handler(message: Message, state: FSMContext):
    # если не была нажата кнопка из клавиатуры после нажатия на кнопку с вопросом
    if message.text not in (inner_buttons_id and buttons_id) and message.text != "Назад":
        try:
            question: str = message.text
            chat_id_group: str = await Database(ChatIDAdmission).get_field_by_name("chat_id")

            button = await group_btn.gen_answer_btn(user_id=message.from_user.id)

            await bot.send_message(chat_id=chat_id_group, text=f"""{datetime.now().strftime("%d.%m.%Y %H:%M")}
Вопрос от <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name} {message.from_user.last_name}</a>

"{question}" """, reply_markup=button
                        )

            await message.answer("Ваш вопрос учтён и отправлен приёмной комиссии. Ожидайте ответа")

        except MultipleObjectsReturned as error:
            await message.answer(f"Ошибка 500. Не удалось отправить сообщение\n{debug(str(error))}")

        except Exception as error:
            await message.answer(f"Произошла неизвестная ошибка\n{debug(str(error))}")
            logging.error(error)

        await state.finish()

    else:
        await message.answer("Выход из режима ввода текста")
        await state.finish()


@dp.message_handler(text="Получить результаты")
async def get_results(message: Message):
    await message.answer("Ваш запрос обрабатывается. Подождите несколько секунд")

    query: dict = await db_commands.get_bak_directions()
    directions = dict(sorted(query.items(), key=lambda k: k[0]))

    result: str = await google_sheets.proftest_results.get_results(str(message.from_user.id), directions)
    try:
        await message.answer(result)

    except MessageTextIsEmpty:
        await message.answer("Вы еще не прошли профориентационный тест")


# * Обработчик клавиатуры первого уровня
@dp.message_handler(lambda message: message.text in keyboard["first"])
async def menu(message: Message, state: FSMContext):
    pressed_button: str = message.text
    btn_id: int = buttons_id[pressed_button]

    type_content: str = InfoPage.objects.get(id=btn_id).type_content

    try:
        comment: str = InfoPage.objects.get(
            id=btn_id
        ).info

        if type_content == "keyboard":
            await message.answer(
                comment, reply_markup=choose_level
            )
            await state.set_state(PositionState.set_pressed_btn)

            async with state.proxy() as data:
                inline_id: str = Page.objects.get(id=btn_id).inline_tag
                data["page"] = inline_id
            await PositionState.next()

        else:
            if pressed_button == "Тест на профориентацию":
                link = f"https://docs.google.com/forms/d/e/1FAIpQLSeNkbEzcvxl7JsUxuYu13ECBLlZZrxJNyBjC_krgnZbVrUcjQ/viewform?usp=pp_url&entry.834901947={message.from_user.id}"
                comment += f"\nСобственно, сам <a href='{link}'>профориентационный тест</a>"

            if not (Page.objects.get(btn_title=pressed_button).file.name is None):
                file_path = Page.objects.get(btn_title=pressed_button).file.path
                logging.info(file_path)

                async with aiofiles.open(file_path, "rb") as photograph:
                    await bot.send_photo(
                        chat_id=message.chat.id, photo=photograph,
                        caption=comment
                    )
            try:
                await message.answer(comment, reply_markup=kb.generate_keyboard(btn_id))
            except CantParseEntities:
                await message.answer("Ошибка! Неправильная разметка информации")

    except MessageTextIsEmpty:
        await message.answer("Информации нет")


# * Обработчик вложенной клавиатуры
@dp.message_handler(lambda message: message.text in keyboard["second"])
async def InnerKeyboardHandler(message: Message, state: FSMContext):
    pressed_button: str = message.text
    btn_id: int = inner_buttons_id[pressed_button]

    type_content: tuple = InnerKeyboard.objects.filter(
        buttons_id=btn_id,
        btn_title=pressed_button
    ).values_list("type_content").last()

    try:
        # * если нажата кнопка с id 'keyboard' -> формирование инлайн клавиатуры
        if type_content[0] == "keyboard":
            information = InnerKeyboard.objects.filter(
                buttons_id=btn_id,
                btn_title=pressed_button
            ).values_list("info").last()

            await message.answer(*information, reply_markup=choose_level)

            await state.set_state(PositionState.set_pressed_btn)

            async with state.proxy() as data:
                inline_id: tuple = InnerKeyboard.objects.filter(
                    btn_title=pressed_button,
                    buttons_id=btn_id
                ).values_list("inline_tag").last()

                data["page"] = inline_id[0]
            await PositionState.next()

        else:
            information = InnerKeyboard.objects.filter(
                buttons_id=btn_id,
                btn_title=pressed_button
            ).values_list("info").last()

            if not (InnerKeyboard.objects.get(btn_title=pressed_button).file.name is None):
                file_path = InnerKeyboard.objects.get(btn_title=pressed_button).file.path
                logging.info(file_path)

                async with aiofiles.open(file_path, "rb") as photograph:
                    await bot.send_photo(
                        chat_id=message.chat.id, photo=photograph,
                        caption=information[0]
                    )
            else:
                try:
                    await message.answer(*information)
                except CantParseEntities:
                    await message.answer("Ошибка! Неправильная разметка информации")

    except MessageTextIsEmpty:
        await message.answer("Информации нет")
