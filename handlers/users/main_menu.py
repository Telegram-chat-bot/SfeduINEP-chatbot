import aiofiles
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils.exceptions import MessageTextIsEmpty, CantParseEntities, PhotoDimensions

from django_admin.bot.models import Page, InfoPage, InnerKeyboard
from filters import CommandBack, OtherWords

from keyboards.inline.buttons import choose_level

from states.state_machine import PositionState
from loader import dp, bot
from utils.debugger import debugger
from aiogram.types import Message

from keyboards.default import enrollee_menu as kb

import logging

from utils import google_sheets
from utils.db_api import db_commands
from utils.bot_commands.commands import commands

from handlers.groups.main_menu_group import group_menu

# * Формирование словаря кнопок первого уровня => кнопка : id
buttons = Page.objects.values("btn_title", "id")
buttons_id: dict = {btn['btn_title']: btn["id"] for btn in buttons}

# * Формирование словаря кнопок второго уровня => кнопка : id
inner_buttons = InnerKeyboard.objects.values("btn_title", "buttons_id")
inner_buttons_id: dict = {btn["btn_title"]: btn["buttons_id"] for btn in inner_buttons}

buttons_title_first = list(buttons_id)
keyboard = {"first": buttons_title_first}

buttons_title_second = list(inner_buttons_id)
keyboard["second"] = buttons_title_second

service_words = [*keyboard["first"], *keyboard["second"], *group_menu, "Назад", *(map(lambda c: f"/{c}", commands))]


# * Обработчик неслужебных слов
@dp.message_handler(OtherWords(service_words))
async def service_words_handler(message: Message):
    """
    Если пользователь ввел сообщение, которое не содержит закрепленные команды или названия кнопок, бот отвечает ему, \
    что не понимает сообщения

    :param message: переменная для манипуляции над сообщениями
    """
    await message.answer("Извините, но я не понимаю вашей команды")


# * Обработчик кнопки Назад
@dp.message_handler(CommandBack())
async def back_to_btn_handler(message: Message):
    """
    Обработчик нажатия кнопки "Назад"

    При нажатии переводит пользователя на уровень ниже

    :param message: переменная для манипуляции над сообщениями
    """
    await message.answer("Вы вернулись назад", reply_markup=await kb.generate_keyboard(
        one_time_keyboard=True
    ))


@dp.message_handler(text="Получить результаты")
async def get_results(message: Message):
    """
    Обработчик нажатия на кнопку "Получить результаты" в разделе "Тест на профориентацию"
    При нажатии обращается к API Google Sheet, для получения результата теста, если таковой имеется
    Если результата нет, бот возвращает пользователю сообщение о его отсутствии

    :param message: переменная для манипуляции над сообщениями
    """
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

            if Page.objects.get(btn_title=pressed_button).file.name not in [None, ""]:
                file_path: str = Page.objects.get(btn_title=pressed_button).file.path

                async with aiofiles.open(file_path, "rb") as photograph:
                    await bot.send_photo(
                        chat_id=message.chat.id, photo=photograph,
                        caption=comment,
                        reply_markup=await kb.generate_keyboard(btn_id)
                    )
            else:
                await message.answer(comment, reply_markup=await kb.generate_keyboard(btn_id))

    except MessageTextIsEmpty as error:
        await message.answer(f"Информации нет\n{debugger(error)}", parse_mode='')

    except PhotoDimensions as error:
        await message.answer(f"Ошибка вывода изображения: большое разрешение\n{debugger(error)}", parse_mode='')
        logging.error(error)

    except CantParseEntities as error:
        await message.answer(f"Ошибка! Неправильная разметка информации\n{debugger(error)}", parse_mode='')
