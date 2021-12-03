from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.filters.builtin import Text
from filters import CommandBack
from loader import dp, pressed_button, bot
from aiogram.types import Message

from aiogram.dispatcher import FSMContext
from states.state_machine import AdminState
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

#ГЛАВНОЕ МЕНЮ--------------
@dp.message_handler(text = "Направления подготовки")
async def prepare_direction_item(message: Message):
    pressed_button.append("dir_inf")
    await message.answer("Выберите специальность", reply_markup=btn.choose_level)
    

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


@dp.message_handler(state='*', commands='exit')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_command(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.finish()
    await message.answer('Выхожу из режима ввода данных...', reply_markup=kb.main_menu)
    

@dp.message_handler(commands="answer")
async def answer_command_handler(message: Message, state: FSMContext):
    admins = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    
    if admins.status in ["creator", "administrator"]:
        logging.info(admins.status)
        await message.answer("Введите id человека, предоставленный в вопросе")
        await state.set_state(AdminState.get_id)
    else:
        await message.answer("Вы не являетесь админом")