from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import dp


@dp.message_handler(Command("exit"), state="*")
async def exit_input_mode(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Ввод текста отменён")
