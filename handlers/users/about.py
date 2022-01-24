from loader import dp, bot
from aiogram.types import Message

from utils.db_api import db_commands
import aiofiles


# РАЗДЕЛ ОБ ИНСТИТУТЕ
@dp.message_handler(text="Знакомство")
async def excursion(message: Message):
    acquaintance = await db_commands.get_about_acquaintance()
    await message.answer(*acquaintance)


@dp.message_handler(text="Записаться на экскурсию")
async def excursion(message: Message):
    excursion = await db_commands.get_about_excursion()
    await message.answer(*excursion)


@dp.message_handler(text="Наука и учёба")
async def science(message: Message):
    science_article = await db_commands.get_about_science()
    await message.answer(*science_article)


@dp.message_handler(text="Мероприятия")
async def events(message: Message):
    events = await db_commands.get_about_events()
    await message.answer(*events)


@dp.message_handler(text="Партнеры и трудоустройство")
async def partners_employment(message: Message):
    partners_work = await db_commands.get_about_partners_work()
    await message.answer(*partners_work)


@dp.message_handler(text="Студсовет")
async def stud_council(message: Message):
    stud_council = await db_commands.get_about_council()
    await message.answer(*stud_council)


@dp.message_handler(text="Карта")
async def excursion(message: Message):
    async with aiofiles.open("static/info/img/map.jpg", "rb") as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Карта общежитий")

    await message.answer("Адрес корпуса ИНЭП")
    await bot.send_location(chat_id=message.chat.id, latitude="47.204529", longitude="38.944375")


@dp.message_handler(text="Фото")
async def photo(message: Message):
    photo_link = await db_commands.get_about_photo()
    await message.answer(*photo_link)


@dp.message_handler(text="Контакты")
async def contacts(message: Message):
    contacts = await db_commands.get_about_contacts()
    await message.answer(*contacts)
