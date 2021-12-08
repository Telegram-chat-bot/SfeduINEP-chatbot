from aiogram.types import CallbackQuery

from loader import dp, bot

from keyboards.inline import buttons as btn


@dp.callback_query_handler(lambda call: call.data in ["back_to", "back_to_menu"])
async def back_btn_handler(call: CallbackQuery):
    if call.data == "back_to":
        await call.message.edit_text("Выберите уровень подготовки", reply_markup=btn.choose_level)
        
    elif call.data == "back_to_menu":
        await call.message.delete_reply_markup()
        await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)