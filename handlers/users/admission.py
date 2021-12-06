import logging
from loader import dp, pressed_button
from aiogram.types import Message

from keyboards.inline import buttons as btn
from keyboards.default import menu as kb

from utils.db_api import db_commands



#РАЗДЕЛ ПОСТУПЛЕНИЕ--------
@dp.message_handler(text = "Правила приема")
async def rules_admission(message: Message):
    admission_rules = await db_commands.get_admission_rules()
    await message.answer(*admission_rules)

@dp.message_handler(text = "Подать документы")
async def submit_doc(message: Message):
    submit_document = await db_commands.get_admission_submit_doc()
    await message.answer(*submit_document)

@dp.message_handler(text = "Проходные баллы")
async def passing_scores(message: Message):
    pressed_button.append("dir_pass")
    await message.answer("Выберите направление подготовки", reply_markup = btn.choose_level)

@dp.message_handler(text = "Количество мест")  #item id = 3
async def num_of_places(message: Message):
    pressed_button.append("num_places")
    await message.answer("Выберите направление подготовки", reply_markup=btn.choose_level)

@dp.message_handler(text = "Индивидуальные достижения")
async def achievements(message: Message):
    achievements = await db_commands.get_admission_achievements()
    await message.answer(*achievements)

@dp.message_handler(text = "Особые права и льготы")
async def special_rights(message: Message):
    special_rights = await db_commands.get_admission_spec_rights()
    await message.answer(*special_rights)

@dp.message_handler(text = "Статистика приёма")
async def admission_statcistics(message: Message):
    statistic = await db_commands.get_admission_stat()
    await message.answer(*statistic)

@dp.message_handler(text = "Порядок зачисления")
async def enrollment_procedure(message: Message):
    enrollment_procedure = await db_commands.get_admission_enrollment_proc()
    await message.answer(*enrollment_procedure)

#---------------------------