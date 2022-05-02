import os

from loader import dp, bot
from aiogram.types import Message

from utils.db_api.db_commands import Database
from django_admin.bot.models import About
import aiofiles

db = Database(About)


# РАЗДЕЛ ОБ ИНСТИТУТЕ
@dp.message_handler(text="Знакомство")
async def acquaintance(message: Message):
    await message.answer(await db.get_field_by_name("acquaintance"))


@dp.message_handler(text="Записаться на экскурсию")
async def excursion(message: Message):
    await message.answer(await db.get_field_by_name("excursion"))


@dp.message_handler(text="Наука и учёба")
async def science(message: Message):
    await message.answer(await db.get_field_by_name("science"))


@dp.message_handler(text="Мероприятия")
async def events(message: Message):
    await message.answer(await db.get_field_by_name("events"))


@dp.message_handler(text="Партнеры и трудоустройство")
async def partners_employment(message: Message):
    await message.answer(await db.get_field_by_name("partners_work"))


@dp.message_handler(text="Студсовет")
async def stud_council(message: Message):
    await message.answer(await db.get_field_by_name("stud_council"))


@dp.message_handler(text="Карта")
async def excursion(message: Message):
    async with aiofiles.open(os.path.join(os.getcwd(), "django_admin/static/info/img/map.jpg"), "rb") as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Карта общежитий")

    await message.answer("Адрес корпуса ИНЭП")
    await bot.send_location(chat_id=message.chat.id, latitude="47.204529", longitude="38.944375")


@dp.message_handler(text="Фото")
async def photo(message: Message):
    await message.answer(await db.get_field_by_name("photo"))


@dp.message_handler(text="Контакты")
async def contacts(message: Message):
    await message.answer(await db.get_field_by_name("contacts"))
