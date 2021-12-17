from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

check_results_btn = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Получить результаты")
        ],
        [
            KeyboardButton("Назад")
        ]
    ],
    resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Тест на профориентацию"),
            KeyboardButton("Направления подготовки"),
        ],
        [
            KeyboardButton("Поступление"),
            KeyboardButton("Об институте"),
            KeyboardButton("Задать вопрос")
        ]
    ],
    resize_keyboard=True
)

university_admission = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Правила приема"), 
            KeyboardButton("Подать документы"),
        ],
        [
            KeyboardButton("Проходные баллы"),  
            KeyboardButton("Количество мест")   
        ],
        [
            KeyboardButton('Индивидуальные достижения'),
            KeyboardButton('Особые права и льготы')
        ],
        [
            KeyboardButton('Статистика приёма'),
            KeyboardButton('Порядок зачисления'),
            KeyboardButton('Назад')
        ]
    ],
    resize_keyboard=True
)

about_university = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Знакомство"),
            KeyboardButton("Записаться на экскурсию"),
            
        ],
        [
            KeyboardButton("Мероприятия"),
            KeyboardButton("Наука и учёба")
        ],
        [
            KeyboardButton("Партнеры и трудоустройство"),
            KeyboardButton("Студсовет")
        ],
        [
            KeyboardButton("Фото"),
            KeyboardButton("Карта"),
            KeyboardButton("Контакты") 
        ],
        [
            KeyboardButton("Назад")
        ]
    ],
    resize_keyboard=True
)


ask_question = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('F.A.Q'),
            KeyboardButton('Вопросы по поступлению'),
            KeyboardButton('Вопросы по направлению подготовки')
        ],
        [
            KeyboardButton("Назад")
        ]
    ],
    resize_keyboard=True
)

