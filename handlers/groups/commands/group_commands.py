from aiogram.dispatcher.storage import FSMContext
from django_admin.bot.models import Directions

from loader import dp, pressed_button, bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline import buttons as btn
from states.state_machine import AdminState
from utils.db_api import db_commands



@dp.message_handler(state=AdminState.get_id)
async def get_user_id(message: Message, state: FSMContext):
    await state.update_data(user_id = message.text)
    await message.answer("Напишите свой ответ")
    
    await AdminState.get_answer.set()
    
@dp.message_handler(state=AdminState.get_answer)
async def send_answer(message: Message, state: FSMContext):
    if message.text != "Назад" or message.text.startswith("/"):
        await state.update_data(answer = message.text)
    
        data = await state.get_data()
    
        await bot.send_message(
            chat_id=data.get("user_id"),
            text=f"""
Вам пришел ответ на ваш ранее заданный вопрос
"{data.get("answer")}"
        """
    )
        await message.answer("Вопрос отправлен абитуриенту")
    await state.finish()
    
    

type_group = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="По поводу поступления", callback_data="adm_type")
        ],
        [
            InlineKeyboardButton(text="По поводу конкретного направления подготовки", callback_data="dp_type")
        ]
    ]
)
        
@dp.message_handler(commands="add_group")
async def add_group(message: Message):
    pressed_button.append("type_group")
    await message.answer("Какого типа ваша группа?", reply_markup=type_group)
    
    
@dp.callback_query_handler(lambda call: call.data in ["adm_type", "dp_type"])
async def type_of_group(call: CallbackQuery):
    if call.data == "adm_type" and db_commands.ChatIDAdmission.objects.count == 0:
        try:
            await db_commands.save_chatId_Group_admission(call.message.chat.id)
            await call.message.answer("Группа успешно занесена в базу данных")
        except Exception:
            await call.message.answer("Ошибка!")
            
    elif call.data == "dp_type":
        key = await btn.gen_directions_btns(level="bak")
        await call.message.edit_text("Выберите ваше направление подготовки", reply_markup=key)
    else:
        await call.message.edit_text("ID чата уже есть в базе данных")
    
    

