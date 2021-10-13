from loader import dp, bot
from aiogram.types import Message, CallbackQuery

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn


@dp.message_handler(commands="start")
async def welcome(message: Message):
    await message.answer("Привет, выбери язык|Hello, choose language|Hola, elige tu idioma", reply_markup=btn.lang_key)


#Обработчики главных разделов---------------
@dp.message_handler(lambda message: message.text == "Направления подготовки")
async def direct_of_training(message: Message):
    await message.answer("Выберите интересующий вас уровень подготовки", reply_markup=btn.choose_level)

@dp.message_handler(lambda message:message.text =="Об институте")
async def about_item(message:Message):
    await message.answer("Временная заглушка",reply_markup=kb.about_university)

@dp.message_handler(lambda message:message.text =="Поступление")
async def admission_item(message:Message):
    await message.answer("Временная заглушка",reply_markup=kb.university_admission)

@dp.message_handler(lambda message:message.text =="Задать вопрос")
async def ask_item(message:Message):
    await message.answer("Временная заглушка",reply_markup=kb.ask_question)

@dp.message_handler(lambda message:message.text =="Назад")
async def back_to_btn(message:Message):
    await message.answer("Вы вернулись назад",reply_markup=kb.abiturient_menu)