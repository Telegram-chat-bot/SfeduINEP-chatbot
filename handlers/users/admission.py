from aiogram.dispatcher import FSMContext
import logging

from loader import dp
from aiogram.types import Message, CallbackQuery

from keyboards.inline import buttons as btn

from states.state_machine import PositionState

from django_admin.bot.models import Admission, Passing_scores, Directions
from utils.db_api.db_commands import Database

db = Database(Admission)


# РАЗДЕЛ ПОСТУПЛЕНИЕ--------
@dp.message_handler(text="Правила приема")
async def rules_admission(message: Message):
    # t: QuerySet = await Database(Passing_scores).get_field_by_id("direction_id", "inf", id=2)
    await message.answer(await db.get_field_by_name("admission_rules"))


@dp.message_handler(text="Подать документы")
async def submit_doc(message: Message):
    await message.answer(await db.get_field_by_name("submit_doc"))


@dp.message_handler(text="Проходные баллы")
async def passing_scores(message: Message, state: FSMContext):
    await message.answer("Выберите направление подготовки", reply_markup=btn.choose_level)

    await state.set_state(PositionState.set_pressed_btn)
    async with state.proxy() as data:
        data["page"] = "pass_score"
    await PositionState.next()


@dp.message_handler(text="Количество мест")
async def num_of_places(message: Message, state: FSMContext):
    await message.answer("Выберите направление подготовки", reply_markup=btn.choose_level)

    await state.set_state(PositionState.set_pressed_btn)
    async with state.proxy() as data:
        data["page"] = "number_of_places"
    await PositionState.next()


@dp.message_handler(text="Индивидуальные достижения")
async def achievements(message: Message):
    await message.answer(await db.get_field_by_name("achievements"))


@dp.message_handler(text="Особые права и льготы")
async def special_rights(message: Message):
    await message.answer(await db.get_field_by_name("special_rights"))


@dp.message_handler(text="Статистика приёма")
async def admission_statistics(message: Message):
    await message.answer(await db.get_field_by_name("admission_stat"))


@dp.message_handler(text="Порядок зачисления")
async def enrollment_procedure(message: Message):
    await message.answer(await db.get_field_by_name("enrollment_proc"))

# ---------------------------
