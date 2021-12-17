import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, CommandStart
from filters import IsGroup, AdminFilter
from loader import dp
from aiogram.types import Message

from keyboards.default import group_menu


@dp.message_handler(Command("exit"), state="*")
async def exit_input_mode(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Ввод текста отменён")


@dp.message_handler(CommandStart(), IsGroup())
async def start_bot(message: Message):
    await message.answer("Вас приветствует чат-бот ИНЭП ЮФУ. "
                         "Выберите интересующий вас пункт ниже",
                         reply_markup=group_menu.main_menu)
