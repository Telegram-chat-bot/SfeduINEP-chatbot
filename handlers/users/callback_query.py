from aiogram.types import CallbackQuery
from loader import dp, bot

from aiogram.types import ReplyKeyboardRemove

from aiogram.utils import markdown as mkn

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn

#Обработчик выбора роли--------------------
@dp.callback_query_handler(lambda call: call.data in ['ru', 'en', 'es'])
async def callback_lang(call: CallbackQuery):
    await call.message.edit_text("Кто вы?", reply_markup=btn.roles)

#Обработчики выбранных ролей-----------------
@dp.callback_query_handler(lambda call: call.data == "abtr")
async def callback_abiturient(call: CallbackQuery):
    await call.message.answer("Выберите интересующий вас пункт", reply_markup=kb.abiturient_menu)
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)

#Направления подготовки-------------
@dp.callback_query_handler(lambda call: call.data in ["bak", "spec", "mag", "back_to"])
async def prepare_direct_block(call: CallbackQuery):
    if call.data == "bak":
        await call.message.edit_text("Направления бакалаврской подготовки:", reply_markup=btn.bak_prepare_direct)
    
    elif call.data == "spec":
        await call.message.edit_text("Специалитет:", reply_markup=btn.spec_prepare_direct)
    elif call.data == "mag":
        await call.message.edit_text("Магистратура", reply_markup=btn.mag_prepare_direct)
    elif call.data == "back_to":
        await call.message.edit_text("Вы вернулись назад", reply_markup=btn.choose_level)
    