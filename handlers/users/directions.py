from loader import dp, db, item

from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, message
from keyboards.inline import buttons as btn

# keyboard = InlineKeyboardMarkup()


# @dp.message_handler(lambda message: message.text == "Направления подготовки") #item id = 1
# async def prepare_direction_item(message: Message):
#     item.append("d1")
#     await message.answer("Выберите специальность", reply_markup=btn.choose_level)

# @dp.callback_query_handler(lambda call: call.data)
# async def direct_of_prepare_handler(call: CallbackQuery):
#     data = await db.get_id(direct="bot_directions")
# #     data = await db.get_direction(block="bot_directions", level=call.data, section="direct_prepare")
# #     for k in data:
# #         keyboard.add(InlineKeyboardButton(text=f"{k.get('name_of_dir')}", callback_data=f"{k.get('direction')}"))
# #     await call.message.answer('test', reply_markup=keyboard)
        
#     #     await call.message.answer(await db.get_direction(level=call.data))
#     # for direction, value in directions[item[-1]].items():
#     #     if call.data == direction:
#     #         if item[-1] == "d1":
#     #             await call.message.edit_text("Всю информацию по данному направлению вы можете найти, перейдя по ссылке", reply_markup=init_url(link=value))
#     #         elif item[-1] in ["d2", "d3"]:
#     #             await call.message.edit_text(f"{direction}\n{value}", reply_markup=InlineKeyboardMarkup().add(btn.back_btn))