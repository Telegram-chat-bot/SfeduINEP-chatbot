from aiogram.dispatcher.filters import CommandStart, Command
from filters import IsGroup
from loader import dp
from aiogram.types import Message

from keyboards.default import group_menu


@dp.message_handler(CommandStart(), IsGroup())
async def start_bot(message: Message):
    await message.answer("Вас приветствует чат-бот ИНЭП ЮФУ. "
                         "Выберите интересующий вас пункт ниже",
                         reply_markup=group_menu.main_menu)


@dp.message_handler(Command("get_id"), IsGroup())
async def get_group_id(message: Message):
    await message.answer(message.chat.id)
