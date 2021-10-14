from loader import dp, bot
from aiogram.types import Message, CallbackQuery

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn


@dp.message_handler(commands="start")
async def welcome(message: Message):
    await message.answer("Привет, выбери язык|Hello, choose language|Hola, elige tu idioma", reply_markup=btn.lang_key)



#Обработчики главных разделов---------------
@dp.message_handler(lambda message: message.text in kb.check)
async def prepare_direct(message: Message):
    await message.answer("Выберите интересующий вас уровень подготовки", reply_markup=btn.choose_level)

@dp.message_handler(lambda message:message.text =="Об институте")
async def callback_level(message:Message):
    await message.answer("Временная заглушка",reply_markup=kb.about_university)

@dp.message_handler(lambda message:message.text =="Поступление")
async def callback_level(message:Message):
    await message.answer("Временная заглушка",reply_markup=kb.university_admission)

@dp.message_handler(lambda message:message.text =="Задать вопрос")
async def callback_level(message:Message):
    await message.answer("Временная заглушка",reply_markup=kb.ask_question)

@dp.message_handler(lambda message:message.text =="Назад")
async def callback_level(message:Message):
    await message.answer("Вы вернулись назад",reply_markup=kb.abiturient_menu)

@dp.message_handler(lambda message:message.text == "Правила приема")
async def pravila_url(message:Message):
    await message.answer("С правилами приема можете ознакомиться ниже",reply_markup = btn.rules)

#пока так
@dp.message_handler(lambda message:message.text == "Направления подготовки")
async def napravlenia(message:Message):
    await message.answer("1 октября будет доступно",reply_markup = btn.training_directions)

#пока так
@dp.message_handler(lambda message:message.text == "Вступительные испытания")
async def napravlenia(message:Message):
    await message.answer("1 октября будет доступно",reply_markup = btn.choose_level)
    if message.text =="Бакалавриат/Специалитет":
        await message.answer("aboba",reply_markup = btn.training_directions)








#@dp.message_handler(lambda message:message.text == "Тест на профориентацию")
#async def callback_level(message:Message):
 #   pass

#@dp.message_handler(lambda message:message.text == "Направления подготовки")
#async def callback_level(message:Message):
 #   pass

#@dp.message_handler(lambda message:message.text == "Вступительные испытания")
#async def callback_level(message:Message):
 #   pass

