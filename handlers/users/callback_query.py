from aiogram.types import CallbackQuery
from loader import dp, bot

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn

@dp.callback_query_handler(lambda call: call.data in ['ru', 'en', 'es'])
async def callback_lang(call: CallbackQuery):
    # choosed_btn = call.data

    await call.message.edit_text("Кто вы?", reply_markup=btn.lang_key)
    await call.message.edit_reply_markup(reply_markup=btn.roles)

@dp.callback_query_handler(lambda call: call.data == "abtr")
async def callback_abiturient(call: CallbackQuery):
    await call.message.answer("Выберите интересующий вас пункт", reply_markup=kb.abiturient_menu)
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)


@dp.callback_query_handler(lambda call: call.data == "bak")
async def bak_choosed(call: CallbackQuery):
    await call.message