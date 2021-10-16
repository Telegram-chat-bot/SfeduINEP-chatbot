from loader import dp, bot
from aiogram.types import Message

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn


@dp.message_handler(commands="start")
async def welcome(message: Message):
    await message.answer("Привет, выбери язык|Hello, choose language|Hola, elige tu idioma", reply_markup=btn.lang_key)


#Уровень Абитуриент--------------
@dp.message_handler(lambda message :message.text =="Об институте")
async def about_item(message:Message):
    await message.answer("Об институте",reply_markup=kb.about_university)

@dp.message_handler(lambda message: message.text =="Поступление")
async def admission_item(message:Message):
    await message.answer("Все о поступлении",reply_markup=kb.university_admission)

@dp.message_handler(lambda message: message.text =="Задать вопрос")
async def ask_item(message:Message):
    await message.answer("Задать вопрос",reply_markup=kb.ask_question)

@dp.message_handler(lambda message: message.text =="Назад")
async def back_to_btn_handler(message:Message):
    await message.answer("Вы вернулись назад",reply_markup=kb.abiturient_menu)

@dp.message_handler(lambda message: message.text == "Направления подготовки")
async def prepare_direction_item(message: Message):
    await message.answer("Выберите специальность", reply_markup=btn.choose_level)


@dp.message_handler(lambda message:message.text == "Вступительные испытания")
async def napravlenia(message:Message):
    await message.answer("Выберите направление подготовки", reply_markup = btn.choose_level)

@dp.message_handler(lambda message:message.text == "Правила приема")
async def pravila_url(message:Message):
    await message.answer("С правилами приема можете ознакомиться ниже",reply_markup = btn.choose_level)