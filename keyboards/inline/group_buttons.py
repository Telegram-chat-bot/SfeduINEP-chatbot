from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

answer_to_question = CallbackData("ask_to", "user_id")
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


async def gen_answer_btn(user_id: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ответить на вопрос", callback_data=answer_to_question.new(user_id=user_id))
            ]
        ]
    )
