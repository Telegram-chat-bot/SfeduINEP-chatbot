from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

group_type = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="По поводу поступления", callback_data="adm_type")
        ],
        [
            InlineKeyboardButton(text="По поводу конкретного направления подготовки", callback_data="dp_type")
        ]
    ]
)