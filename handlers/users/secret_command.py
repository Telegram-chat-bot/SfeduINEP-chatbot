from aiogram.types import Message

from loader import dp

@dp.message_handler(commands="get_id")
async def get_id_cmd(message: Message):
    await message.answer(f"Айди этой группы: {message.chat.id}")