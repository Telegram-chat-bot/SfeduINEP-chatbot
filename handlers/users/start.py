from aiogram.dispatcher.storage import FSMContext
from aiogram.types.message import ContentType

from aiogram.dispatcher.filters import CommandStart
from filters import CommandBack
from loader import dp, pressed_button
from aiogram.types import Message

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn
from utils.db_api import db_commands
import logging


#СТАРТОВОЕ СООБЩЕНИЕ
@dp.message_handler(CommandStart())
async def welcome(message: Message):
    await message.answer(
        await db_commands.get_welcome_msg(),
        reply_markup=kb.main_menu
    ) 
    logging.info(await db_commands.get_chat_id_group("11.03.04"))

#ГЛАВНОЕ МЕНЮ--------------
@dp.message_handler(text = "Направления подготовки")
async def prepare_direction_item(message: Message):
    pressed_button.append("dir_inf")
    await message.answer("Выберите специальность", reply_markup=btn.choose_level)
    
@dp.message_handler(text = "Поступление")
async def admission_item(message:  Message):
    await message.answer("Все о поступлении", reply_markup=kb.university_admission)

@dp.message_handler(text = "Об институте")
async def about_item(message: Message):
    await message.answer("Об институте", reply_markup=kb.about_university)

@dp.message_handler(text = "Задать вопрос")
async def ask_item(message:Message):
    await message.answer("Задать вопрос", reply_markup=kb.ask_question)

#-----------------------------------------

@dp.message_handler(CommandBack())
async def back_to_btn_handler(message: Message):
    await message.answer("Вы вернулись назад", reply_markup=kb.main_menu)
