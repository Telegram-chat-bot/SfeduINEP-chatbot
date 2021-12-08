from aiogram.dispatcher.filters import CommandStart
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from django_admin.bot.models import ChatIDAdmission
from loader import dp, bot
from aiogram.types import Message, CallbackQuery, message

from aiogram.dispatcher import FSMContext
from states.state_machine import AdminState

import logging

from utils.db_api import db_commands

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn


#СТАРТОВОЕ СООБЩЕНИЕ
@dp.message_handler(CommandStart())
async def welcome(message: Message):
    await message.answer(
        await db_commands.get_welcome_msg(),
        reply_markup=kb.main_menu
    )

#КОМАНДА ВЫХОДА ИЗ РЕЖИМА ВВОДА
@dp.message_handler(state='*', commands='exit')
async def cancel_command(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.finish()
    await message.answer('Выхожу из режима ввода данных...')
    
#КОМАНДА ОТВЕТА АБИТУРИЕНТУ
@dp.message_handler(commands="answer")
async def answer_command_handler(message: Message, state: FSMContext):
    if message.chat.type in ["supergroup", "group"]:
        admins = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        
        if admins.status in ["creator", "administrator"]:
            logging.info(admins.status)
            await message.answer("Введите id человека, предоставленный в вопросе")
            await state.set_state(AdminState.get_id)
        else:
            await message.answer("Вы не являетесь админом")
    else:
        await message.answer("У вас здесь нет власти¯\_(ツ)_/¯")
        
        
@dp.message_handler(commands="get_id")
async def get_id_cmd(message: Message):
    if message.chat.type in ["group", "supergroup"]:
        await message.answer(f"Айди этой группы: {message.chat.id}")
    else:
        await message.answer("Команда не предназначена для абитуриента")
    
    
@dp.message_handler(commands="help")
async def help_command(message: Message):
    logging.info(message.chat.type)
    if message.chat.type not in ["group", "supergroup"]:
        await message.answer(
            """
Краткий экскурс в команды бота:
/exit - команда, которая позволяет выйти из режима ввода данных боту (отмена этого действия)
Другие неуказанные команды, кроме start и help, не предназначены для абитуриента.
    
Бот позволяет абитуриенту:
1. Пройти профориентационный тест
2. Узнать проходные баллы, количество мест по тому или иному направлению
3. Изучить ИНЭП
    """
        )
    else:
        await message.answer(
            """
Краткий экскурс в команды бота:
/exit - команда, которая позволяет выйти из режима ввода данных боту (отмена этого действия);
/answer - команда для админов групп, связанных с направлениями ИНЭП, позволящая оперативно ответить на вопрос абитуриента;
/get_id - команда для получения id группы, необходимого для занесения ее в базу данных;
            """
        )



