from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Сделать объявление абитуриентам"),
            KeyboardButton("Помощь")
        ],
        [
            KeyboardButton("Занести группу в базу данных"),
            KeyboardButton("Удалить группу из базы данных")
        ]
    ],
    resize_keyboard=True
)