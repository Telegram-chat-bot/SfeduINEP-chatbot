from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

back_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("Назад")]
    ],
    resize_keyboard=True
)


abiturient_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Тест на профориентацию"),
            KeyboardButton("Направления подготовки"),
            KeyboardButton("Вступительные испытания"),
            
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
        ],
    ],
    resize_keyboard=True
)



about_university = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Записаться на экскурсию"),
            KeyboardButton("Наука и учеба"),
            
        ],
        [
            KeyboardButton("Мероприятия"),
            KeyboardButton("Спорт и культура")
        ],
        [
            KeyboardButton('Конкурсы'),
            KeyboardButton('Партнеры и трудоустройство')
        ],
        [
            KeyboardButton('Новости'),
            KeyboardButton('Общежития и столовые')
        ],
        [
            KeyboardButton('Фото'),
            KeyboardButton('Контакты'),
            KeyboardButton('Назад')
        ]
    ],
    resize_keyboard=True
)


ask_question = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('F.A.Q')
        ],
        [
            KeyboardButton('Вопросы по поступлению')
        ],
        [
            KeyboardButton('Вопросы по направлению подготовки'),
            KeyboardButton("Назад")
        ]
    ],
    resize_keyboard=True
)

