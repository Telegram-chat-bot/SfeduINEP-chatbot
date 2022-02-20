import os

from loader import dp, bot
from aiogram.types import Message

from utils.db_api.db_commands import AboutData
import aiofiles


# РАЗДЕЛ ОБ ИНСТИТУТЕ
@dp.message_handler(text="Знакомство")
async def acquaintance(message: Message):
    await message.answer(await AboutData.acquaintance())


@dp.message_handler(text="Записаться на экскурсию")
async def excursion(message: Message):
    await message.answer(await AboutData.excursion())


@dp.message_handler(text="Наука и учёба")
async def science(message: Message):
    await message.answer(await AboutData.science())


@dp.message_handler(text="Мероприятия")
async def events(message: Message):
    await message.answer(await AboutData.events())


@dp.message_handler(text="Партнеры и трудоустройство")
async def partners_employment(message: Message):
    await message.answer(await AboutData.partners_work())


@dp.message_handler(text="Студсовет")
async def stud_council(message: Message):
    await message.answer(await AboutData.council())


@dp.message_handler(text="Карта")
async def excursion(message: Message):
    async with aiofiles.open(os.path.join(os.getcwd(), "static/info/img/map.jpg"), "rb") as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Карта общежитий")

    await message.answer("Адрес корпуса ИНЭП")
    await bot.send_location(chat_id=message.chat.id, latitude="47.204529", longitude="38.944375")


@dp.message_handler(text="Фото")
async def photo(message: Message):
    await message.answer(await AboutData.photo())


@dp.message_handler(text="Контакты")
async def contacts(message: Message):
    await message.answer(await AboutData.contacts())