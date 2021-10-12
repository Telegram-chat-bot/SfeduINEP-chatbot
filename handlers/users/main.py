from loader import dp, bot
from aiogram.types import Message, CallbackQuery

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn


@dp.message_handler(commands="start")
async def welcome(message: Message):
    await message.answer("Привет, выбери язык|Hello, choose language|Hola, elige tu idioma", reply_markup=btn.lang_key)

#Выбор языка---------
@dp.callback_query_handler(lambda call: call.data in ['ru', 'en', 'es'])
async def callback_lang(call: CallbackQuery):
    choosed_btn = call.data

    await call.message.edit_text("Кто вы?", reply_markup=btn.lang_key)
    await call.message.edit_reply_markup(reply_markup=btn.roles)

@dp.callback_query_handler(lambda call: call.data == "abtr")
async def callback_abiturient(call: CallbackQuery):
    await call.message.answer("Выберите интересующее вас в меню ниже", reply_markup=kb.abiturient_menu)
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)


@dp.message_handler(lambda message:message.text =="Об институте")
async def callback_level(message:Message):
    await message.answer("Все о университете",reply_markup=kb.about_university)

@dp.message_handler(lambda message:message.text =="Поступление")
async def callback_level(message:Message):
    await message.answer("Все о поступлении",reply_markup=kb.flow_in_university)

@dp.message_handler(lambda message:message.text =="Задать вопрос")
async def callback_level(message:Message):
    await message.answer("Задать вопрос",reply_markup=kb.ask_question)

@dp.message_handler(lambda message:message.text =="Назад")
async def callback_level(message:Message):
    await message.answer("возвращение",reply_markup=kb.abiturient_menu)




#@dp.message_handler(lambda message:message.text == "Тест на профориентацию")
#async def callback_level(message:Message):
 #   pass

#@dp.message_handler(lambda message:message.text == "Направления подготовки")
#async def callback_level(message:Message):
 #   pass

#@dp.message_handler(lambda message:message.text == "Вступительные испытания")
#async def callback_level(message:Message):
 #   pass

