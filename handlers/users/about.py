from loader import dp, bot
from aiogram.types import Message

from utils.db_api.db_commands import get_about_data
import asyncio

loop = asyncio.get_event_loop()
data = loop.run_until_complete(get_about_data())[0]


#РАЗДЕЛ ОБ ИНСТИТУТЕ
@dp.message_handler(text = "Знакомство")
async def excursion(message: Message):
    await message.answer(data["acquaintance"])

@dp.message_handler(text = "Записаться на экскурсию")
async def excursion(message: Message):
    await message.answer(data["excursion"])

@dp.message_handler(text = "Наука и учёба")
async def science(message: Message):
    await message.answer(data["science"])

@dp.message_handler(text = "Мероприятия")
async def events(message: Message):
    await message.answer(data["events"])

@dp.message_handler(text = "Партнеры и трудоустройство")
async def partners_employment(message: Message):
    await message.answer(data["partners_work"])

@dp.message_handler(text = "Студсовет")
async def stud_council(message: Message):
    await message.answer(data["stud_council"])

@dp.message_handler(text = "Карта")
async def excursion(message: Message):
    with open("img/map.jpg", "rb") as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await bot.send_location(chat_id=message.chat.id, latitude="47.208399", longitude="38.936603")

@dp.message_handler(text = "Фото")
async def photo(message: Message):
    await message.answer(data["photo"])

@dp.message_handler(text = "Контакты")
async def contacts(message: Message):
    await message.answer(data["contacts"])
