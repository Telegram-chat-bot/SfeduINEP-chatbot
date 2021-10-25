from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_btn = InlineKeyboardButton(text="Назад", callback_data="back_to")
#Инлайн кнопки выбора языка---------

lang_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Русский", callback_data="ru"),
            InlineKeyboardButton(text="English", callback_data="en"),
            InlineKeyboardButton(text="Espanol", callback_data="es")
        ]
    ]
)

# Инлайн кнопки выбора ролей--------
roles = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Абитуриент", callback_data="abtr"),
            InlineKeyboardButton(text="Студент", callback_data="std"),
            InlineKeyboardButton(text="Преподаватель", callback_data="tch")
        ]
    ]
)

#Инлайн кнопки выбора уровня образования----------
choose_level = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Бакалавриат", callback_data="bak"),
            InlineKeyboardButton(text="Специалитет", callback_data="spec"),
            InlineKeyboardButton(text="Магистратура", callback_data="mag")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back_to_menu")
        ]
    ]
)
#СПЕЦИАЛЬНОСТИ -----------
#Специальности бакалавра


bak_prepare_direct = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="11.03.03 «Конструирование и технология электронных средств»", callback_data="11.03.03")
            ],
            [
                InlineKeyboardButton(text="11.03.04 «Электроника и наноэлектроника»", callback_data="11.03.04")
            ],
            [
                InlineKeyboardButton(text="12.03.01 «Приборостроение»", callback_data="12.03.01")
            ],
            [
                InlineKeyboardButton(text="12.03.04 «Биотехнические системы и технологии»", callback_data="12.03.04")
            ],
            [
                InlineKeyboardButton(text="20.03.01 «Техносферная безопасность»", callback_data="20.03.01")
            ],
            [
                InlineKeyboardButton(text="28.03.02 «Наноинженерия»", callback_data="28.03.02")
            ],
            [
                back_btn
            ]
    ]
)

#Специалитет 
spec_prepare_direct = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="26.05.04 «Применение и эксплуатация технических систем надводных кораблей и подводных лодок»", callback_data="26.05.04")
        ],
        [
            back_btn
        ]
    ],
    row_width=1
)

#Магистратура


mag_prepare_direct = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="09.04.03 «Прикладная информатика»", callback_data="09.04.03")
        ],
        [
            InlineKeyboardButton(text="11.04.00 «Электроника, радиотехника и системы связи»", callback_data="11.04.00")
        ],
        [
            InlineKeyboardButton(text="12.04.00 «Фотоника, приборостроение, оптические и биотехнические системы и технологии»", callback_data="12.04.00")
        ],
        [
            InlineKeyboardButton(text="28.04.01 «Техносферная безопасность»", callback_data="20.04.01")
        ],
        [
            InlineKeyboardButton(text="28.04.02 «Наноинженерия»", callback_data="28.04.02")
        ],
        [
            back_btn
        ]
    ]
)

#-------------------------------