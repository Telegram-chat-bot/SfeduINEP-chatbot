from aiogram.types import CallbackQuery
from aiogram.types.message import Message

from loader import dp, bot

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn


@dp.callback_query_handler(lambda call: call.data in ["back_to", "back_to_menu"])
async def back_btn_handler(call: CallbackQuery):
    if call.data == "back_to":
        await call.message.edit_text("Выберите уровень подготовки", reply_markup=btn.choose_level)
        
    elif call.data == "back_to_menu":
        await call.message.delete_reply_markup()
        await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)
        
#Направления подготовки-------------
# @dp.callback_query_handler(lambda call: call.data in ["bak", "spec", "mag", "back_to", "back_to_menu"])
# async def prepare_direct_block(call: CallbackQuery):
#     if call.data == "bak":
#         await call.message.edit_text("Направления бакалаврской подготовки:", reply_markup=btn.bak_prepare_direct)
#     elif call.data == "spec":
#         await call.message.edit_text("Направления специалитета:", reply_markup=btn.spec_prepare_direct)
#     elif call.data == "mag":
#         await call.message.edit_text("Направления магистерской подготовки:", reply_markup=btn.mag_prepare_direct)
        
#     elif call.data == "back_to":
#         await call.message.edit_text("Выберите направление подготовки", reply_markup=btn.choose_level)

#     elif call.data == "back_to_menu":
#         await call.message.delete_reply_markup()
#         await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)