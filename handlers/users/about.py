import data
from loader import dp, bot
from aiogram.types import Message
from utils.db_api.db_commands import get_about_data


#РАЗДЕЛ ОБ ИНСТИТУТЕ
@dp.message_handler(lambda message: message.text == "Знакомство")
async def excursion(message: Message):
    data = await get_about_data("acquaintance")
    await message.answer(data[0][0])
    # await message.answer(await db.get_data(block="bot_about", element="acquaintance"))

@dp.message_handler(lambda message: message.text == "Записаться на экскурсию")
async def excursion(message: Message):
    data = await get_about_data("excursion")
    await message.answer(data[0][0])
    # await message.answer(await db.get_data(block="bot_about", element="excursion"))

@dp.message_handler(lambda message: message.text == "Наука и учёба")
async def science(message: Message):
    data = await get_about_data("science")
    await message.answer(data[0][0])
    # await message.answer(await db.get_data(block="bot_about", element="science"))

@dp.message_handler(lambda message: message.text == "Мероприятия")
async def events(message: Message):
    data = await get_about_data("events")
    await message.answer(data[0][0])
    # await message.answer(await db.get_data(block="bot_about", element="events"))

@dp.message_handler(lambda message: message.text == "Партнеры и трудоустройство")
async def partners_employment(message: Message):
    data = await get_about_data("partners_work")
    await message.answer(data[0][0])
    # await message.answer(await db.get_data(block="bot_about", element="partners_work"))

@dp.message_handler(lambda message: message.text == "Студсовет")
async def stud_council(message: Message):
    data = await get_about_data("stud_council")
    await message.answer(data[0][0])
    # await message.answer(await db.get_data(block="bot_about", element="stud_council"))

@dp.message_handler(lambda message: message.text == "Карта")
async def excursion(message: Message):
    await bot.send_location(chat_id=message.chat.id, latitude="47.208399", longitude="38.936603")

@dp.message_handler(lambda message: message.text == "Фото")
async def photo(message: Message):
    data = await get_about_data("photo")
    await message.answer(data[0][0])
    # await message.answer(await db.get_data(block="bot_about", element="photo"))

@dp.message_handler(lambda message: message.text == "Контакты")
async def contacts(message: Message):
    data = await get_about_data("contacts")
    await message.answer(data[0][0])
    # await message.answer(await db.get_data(block="bot_about", element="contacts"))