from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup
from django.db.models import QuerySet

from django_admin.bot.models import Page, InnerKeyboard


def generate_keyboard(btn_id: int = None, one_time_keyboard: bool = False) -> ReplyKeyboardMarkup:
    buttons = Page.objects.values("btn_title", "row")
    keyboard = {}

    if btn_id:
        buttons = InnerKeyboard.objects.filter(buttons_id=btn_id).values("btn_title", "row").order_by("buttons_id")

    for button in buttons:
        if button["row"] not in keyboard:
            keyboard[button["row"]] = [button["btn_title"]]
        else:
            keyboard[button["row"]] += [button["btn_title"]]

    main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=one_time_keyboard)

    for btn in keyboard.values():
        main_menu.row(*btn)

    main_menu.row("Назад") if btn_id else None

    return main_menu


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