from aiogram.bot.api import check_result
from aiogram.types import CallbackQuery, message
from loader import dp, bot

from os import path, listdir

from aiogram.utils import markdown as mkn

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn

@dp.callback_query_handler(lambda call: call.data in ['ru', 'en', 'es'])
async def callback_lang(call: CallbackQuery):
    await call.message.edit_text("Кто вы?", reply_markup=btn.lang_key)
    await call.message.edit_reply_markup(reply_markup=btn.roles)

@dp.callback_query_handler(lambda call: call.data == "abtr")
async def callback_abiturient(call: CallbackQuery):
    await call.message.answer("Выберите интересующий вас пункт", reply_markup=kb.abiturient_menu)
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)

#Направления подготовки-------------
@dp.callback_query_handler(lambda call: call.data in ["bak", "mag"])
async def bak(call: CallbackQuery):
    await call.message.edit_text("Выберите направление подготовки", reply_markup=btn.choose_level)
    await call.message.edit_reply_markup(reply_markup=btn.bak_prepare_direct)
    
    # dir = f"img\\{call.data}\\prepare_direct"
    # file = listdir(dir)[0]

    # with open(path.join(dir, file), "rb") as photo:
    #     await call.message.answer_photo(photo=photo, caption="<a href='https://sfedu.ru/www/stat_pages22.show?p=ELS/inf/D&x=ELS/-3000000000872'>Источник</a>")
    #     await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)