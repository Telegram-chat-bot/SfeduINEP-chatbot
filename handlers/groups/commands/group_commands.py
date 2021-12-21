import logging

from aiogram.dispatcher.filters import CommandStart
from filters import IsGroup
from loader import dp
from aiogram.types import Message

from keyboards.default import group_menu


@dp.message_handler(CommandStart(), IsGroup())
async def start_bot(message: Message):
    await message.answer("Вас приветствует чат-бот ИНЭП ЮФУ. "
                         "Выберите интересующий вас пункт ниже",
                         reply_markup=group_menu.main_menu)
