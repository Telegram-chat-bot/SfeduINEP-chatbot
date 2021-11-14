from loader import dp, item

from aiogram.types import Message

from keyboards.inline import buttons as btn

from utils.db_api.db_commands import get_admission_data
import asyncio

loop = asyncio.get_event_loop()

data = loop.run_until_complete(get_admission_data())[0]

#РАЗДЕЛ ПОСТУПЛЕНИЕ--------
@dp.message_handler(text = "Правила приема")
async def rules_admission(message: Message):
    await message.answer(data["admission_rules"])

@dp.message_handler(text = "Подать документы")
async def submit_doc(message: Message):
    await message.answer(data["submit_doc"])

@dp.message_handler(text = "Проходные баллы")
async def passing_scores(message: Message):
    item.append("d2")
    await message.answer("Выберите направление подготовки", reply_markup = btn.choose_level)

@dp.message_handler(text = "Количество мест")  #item id = 3
async def num_of_places(message: Message):
    item.append("d3")
    await message.answer("Выберите направление подготовки", reply_markup=btn.choose_level)

@dp.message_handler(text = "Индивидуальные достижения")
async def achievements(message: Message):
    await message.answer(data["achievements"])

@dp.message_handler(text = "Особые права и льготы")
async def special_rights(message: Message):
    await message.answer(data["special_rights"])

@dp.message_handler(text = "Статистика приёма")
async def admission_statcistics(message: Message):
    await message.answer(data["admission_stat"])

@dp.message_handler(text = "Порядок зачисления")
async def enrollment_procedure(message: Message):
    await message.answer(data["enrollment_proc"])

#---------------------------