from aiogram.dispatcher.storage import FSMContext
from filters import CommandBack
from states.state_machine import PositionState
from loader import dp
from aiogram.types import Message

from keyboards.default import enrollee_menu as kb
from keyboards.inline import buttons as btn

from utils.db_api import db_commands
import logging

# ГЛАВНОЕ МЕНЮ--------------
from utils.db_api import db_commands


@dp.message_handler(text="Поступление")
async def admission_item(message: Message):
    await message.answer("В этом разделе вы можете узнать о различных тонкостях и нюансах поступления",
                         reply_markup=kb.university_admission)


@dp.message_handler(text="Направления подготовки")
async def prepare_direction_item(message: Message, state: FSMContext):
    await message.answer("Выберите специальность", reply_markup=btn.choose_level)

    await state.set_state(PositionState.set_pressed_btn)
    async with state.proxy() as data:
        data["page"] = "inf_dir"
    await PositionState.next()


@dp.message_handler(text="Записаться на День открытых дверей")
async def open_day_item(message: Message):
    await message.answer(*await db_commands.openday_inf(), reply_markup=kb.main_menu)


@dp.message_handler(text="Об институте")
async def about_item(message: Message):
    await message.answer("Тут вы можете узнать все что угодно об ИНЭП", reply_markup=kb.about_university)


@dp.message_handler(text="Задать вопрос")
async def ask_item(message: Message):
    await message.answer(
        "Здесь вы можете просмотреть ответы на часто задаваемые вопросы, а также задать вопрос непосредственно "
        "приемной комиссии и руководителям направления",
        reply_markup=kb.ask_question)


# -----------------------------------------

@dp.message_handler(CommandBack())
async def back_to_btn_handler(message: Message):
    await message.answer("Вы вернулись назад", reply_markup=kb.main_menu)
