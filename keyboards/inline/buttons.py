from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Правила приема", callback_data="admission-admission_rules"),
            InlineKeyboardButton(text="Подать документы", callback_data="admission-submit_doc"),
            InlineKeyboardButton(text="Проходные баллы", callback_data="admission-passing_scores")
        ],
        [
            InlineKeyboardButton(text="Количество мест", callback_data="admission-number_of_places"),
            InlineKeyboardButton(text="Индивидуальные достижения", callback_data="admission-achievements"),
            InlineKeyboardButton(text="Особые права и льготы", callback_data="admission-special_rights")
        ],
        [
            InlineKeyboardButton(text="Статистика приема", callback_data="admissions-admission_stat"),
            InlineKeyboardButton(text="Порядок зачисления", callback_data="admission-enrollment_proc"),
            InlineKeyboardButton(text="Знакомство", callback_data="about-acquaintance")
        ],
        [
            InlineKeyboardButton(text="Записаться на экскурсию", callback_data="about-excursion"),
            InlineKeyboardButton(text="Мероприятия", callback_data="about-events"),
            InlineKeyboardButton(text="Наука и учёба", callback_data="about-science")
        ],
        [
            InlineKeyboardButton(text="Партнеры и трудоустройство", callback_data="about-partners_work"),
            InlineKeyboardButton(text="Студсовет", callback_data="about-stud_council"),
            InlineKeyboardButton(text="Фото", callback_data="about-photo")
        ],
        [
            InlineKeyboardButton(text="Карта", callback_data="about-map"),
            InlineKeyboardButton(text="Контакты", callback_data="about-contacts"),
            InlineKeyboardButton(text="FAQ", callback_data="questions-faq")
        ]
    ]
)

back_btn = InlineKeyboardButton(text="Назад", callback_data="back_to")

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
    inline_keyboard =
    [
      
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
            InlineKeyboardButton(text="21.03.02 «Землеустройство и кадастры»", callback_data="21.03.02")
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

