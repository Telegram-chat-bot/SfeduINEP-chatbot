from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Ответить на вопрос"),
            KeyboardButton("Помощь")
        ],
        [
            KeyboardButton("Занести группу в базу данных"),
            KeyboardButton("Удалить группу из базы данных")
        ]
    ],
    resize_keyboard=True
)