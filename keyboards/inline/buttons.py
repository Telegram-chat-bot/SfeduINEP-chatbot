from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.db_commands import get_directions

back_btn = InlineKeyboardButton(text="Назад", callback_data="back_to")
back_btn_init = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            back_btn
        ]
    ]
)

#Инлайн кнопки выбора уровня образования----------
choose_level = InlineKeyboardMarkup(
    inline_keyboard=[
        [
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
        ],
        [
            InlineKeyboardButton(
                text="Назад",
                callback_data="back_to_menu"
            )
        ]
    ],
    row_width=1,
)

#СПЕЦИАЛЬНОСТИ -----------
#Специальности бакалавра
async def gen_directions_btns_bak(level: str):
    buttons = InlineKeyboardMarkup(row_width=1)
    data = await get_directions()
    for el in data:
        if el["level"] == level:
            buttons.add(InlineKeyboardButton(text=f"{el['direction']} - {el['name_of_dir']}", callback_data=el['direction']))
    buttons.add(back_btn)
    
    return buttons


async def init_url(link):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Ссылка", url=link),
        back_btn
    )
    return keyboard

#-------------------------------

