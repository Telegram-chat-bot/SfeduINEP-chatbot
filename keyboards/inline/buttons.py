from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from django_admin.bot.models import Directions
from utils.db_api.db_commands import Database

db = Database(Directions)

back_btn = InlineKeyboardButton(text="Назад", callback_data="back_to")
back_btn_init = InlineKeyboardMarkup(inline_keyboard=[[back_btn]])

direction_button = CallbackData("direction", "code", "level", "page")

# Инлайн кнопки выбора уровня образования----------
choose_level = InlineKeyboardMarkup(row_width=1)
choose_level.row(
    InlineKeyboardButton(
        text="Бакалавриат",
        callback_data="bak"
    ),
    InlineKeyboardButton(
        text="Специалитет",
        callback_data="spec"
    ),
    InlineKeyboardButton(
        text="Магистратура",
        callback_data="mag"
    )
)
choose_level.row(
    InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_menu"
    )
)


async def gen_directions_btn(level: str, page: str) -> InlineKeyboardMarkup:
    # инициализация клавиатуры
    buttons = InlineKeyboardMarkup(row_width=1)
    data = await db.get_collection_data(is_dict=True)
    for el in data:
        if el["level"] == level:
            button = InlineKeyboardButton(
                text=f"{el['direction']} - {el['name_of_dir']}",
                callback_data=direction_button.new(code=el["direction"], level=level, page=page)
            )
            buttons.add(button)
    buttons.add(back_btn)
    return buttons


async def init_url(link: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Ссылка", url=link),
        back_btn
    )
    return keyboard
