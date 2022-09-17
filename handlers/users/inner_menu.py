import logging

import aiofiles
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.utils.exceptions import MessageTextIsEmpty, PhotoDimensions, CantParseEntities

from django_admin.bot.models import InnerKeyboard
from handlers.users.main_menu import keyboard, inner_buttons_id
from keyboards.inline.buttons import choose_level

from loader import dp, bot
from states.state_machine import PositionState
from utils.debugger import debugger


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
            information: tuple = InnerKeyboard.objects.filter(
                buttons_id=btn_id,
                btn_title=pressed_button
            ).values_list("info").last()

            if InnerKeyboard.objects.get(btn_title=pressed_button).file.name not in [None, ""]:
                file_path: str = InnerKeyboard.objects.get(btn_title=pressed_button).file.path

                async with aiofiles.open(file_path, "rb") as photograph:
                    await bot.send_photo(
                        chat_id=message.chat.id, photo=photograph,
                        caption=information[0]
                    )
            else:
                await message.answer(*information)

    except MessageTextIsEmpty as error:
        await message.answer(f"Информации нет\n{debugger(error)}", parse_mode='')

    except PhotoDimensions as error:
        await message.answer(f"Ошибка вывода изображения: большое разрешение\n{debugger(error)}", parse_mode='')
        logging.error(error)

    except CantParseEntities as error:
        await message.answer(f"Ошибка! Неправильная разметка информации\n{debugger(error)}", parse_mode='')

    except FileNotFoundError:
        await message.answer(InnerKeyboard.objects.filter(
                buttons_id=btn_id,
                btn_title=pressed_button
            ).values_list("info").last()[0])
