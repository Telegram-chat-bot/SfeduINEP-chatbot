from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

group_type = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Поступление", callback_data="adm_type")
        ],
        [
            InlineKeyboardButton(text="Группа по направлению подготовки", callback_data="dp_type")
        ]
    ]
)