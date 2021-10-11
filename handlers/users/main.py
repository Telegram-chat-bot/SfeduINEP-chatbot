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

    await call.message.edit_text("Кто вы?", reply_markup=btn.lang_key)
    await call.message.edit_reply_markup(reply_markup=btn.roles)

@dp.callback_query_handler(lambda call: call.data == "abtr")
async def callback_abiturient(call: CallbackQuery):
    await call.message.answer("Выберите интересующее вас в меню ниже", reply_markup=kb.abiturient_menu)
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)