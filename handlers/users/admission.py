from loader import dp, bot, item, db

from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from keyboards.inline import buttons as btn

#РАЗДЕЛ ПОСТУПЛЕНИЕ--------
@dp.message_handler(lambda message: message.text == "Правила приема")
async def rules_admission(message: Message):
    await message.answer(await db.get_data(block="bot_admission", element="admission_rules"))

@dp.message_handler(lambda message:message.text == "Подать документы")
async def submit_doc(message: Message):
    await message.answer(await db.get_data(block="bot_admission", element="submit_doc"))

@dp.message_handler(lambda message: message.text == "Проходные баллы")
async def passing_scores(message: Message):
    item.append("d2")
    await message.answer("Выберите направление подготовки", reply_markup = btn.choose_level)

@dp.message_handler(lambda message: message.text == "Количество мест")  #item id = 3
async def num_of_places(message: Message):
    item.append("d3")
    await message.answer("Выберите направление подготовки", reply_markup=btn.choose_level)

@dp.message_handler(lambda message: message.text == "Индивидуальные достижения")
async def achievements(message: Message):
    await message.answer(await db.get_data(block="bot_admission", element="achievements"))

@dp.message_handler(lambda message: message.text == "Особые права и льготы")
async def special_rights(message: Message):
    await message.answer(await db.get_data(block="bot_admission", element="special_rights"))

@dp.message_handler(lambda message: message.text == "Статистика приёма")
async def admission_statcistics(message: Message):
    links = [f"https://inep.sfedu.ru/statistika-za-20{y}-god/" for y in range(18, 21)]

    await message.answer("Статистику приёма за прошлые годы вы можете просмотреть по следующим ссылкам\n" + "\n".join(list(set(links))))

@dp.message_handler(lambda message: message.text == "Порядок зачисления")
async def enrollment_procedure(message: Message):
    await message.answer(await db.get_data(block="bot_admission", element="enrollment_proc"))

#---------------------------