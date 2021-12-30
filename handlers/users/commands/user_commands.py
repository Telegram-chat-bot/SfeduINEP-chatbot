from aiogram.dispatcher.filters import CommandStart, Command

from filters.ChatTypeFilter import IsChat
from loader import dp
from aiogram.types import Message

from utils.db_api import db_commands

from keyboards.default import enrollee_menu as kb


# СТАРТОВОЕ СООБЩЕНИЕ
@dp.message_handler(IsChat(), CommandStart())
async def welcome(message: Message):
    await message.answer(
        await db_commands.get_welcome_msg(),
        reply_markup=kb.main_menu
    )

    await db_commands.add_user(
        name=' '.join(
            [
                message.from_user.first_name or "",
                message.from_user.last_name or ""
            ]
        ),
        uid=int(message.from_user.id)
    )


@dp.message_handler(IsChat(), Command("help"))
async def help_command(message: Message):
    await message.answer(
        """
Краткий экскурс в команды бота:
/exit - команда, которая позволяет выйти из режима ввода данных боту (отмена этого действия)
    
Бот позволяет абитуриенту:
1. Пройти профориентационный тест
2. Узнать проходные баллы, количество мест по тому или иному направлению
3. Задать вопрос приемной комиссии или руководителю направления
"""
    )
