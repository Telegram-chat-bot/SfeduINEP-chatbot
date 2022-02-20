import logging

from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram.types import Message, CallbackQuery

from keyboards.inline import buttons as btn
from keyboards.default import enrollee_menu as kb
from states.state_machine import PositionState

from utils.db_api.db_commands import AdmissionData
import asyncio


# РАЗДЕЛ ПОСТУПЛЕНИЕ--------
@dp.message_handler(text="Правила приема")
async def rules_admission(message: Message):
    await message.answer(await AdmissionData.admission_rules())


@dp.message_handler(text="Подать документы")
async def submit_doc(message: Message):
    await message.answer(await AdmissionData.submit_doc())


@dp.message_handler(text="Проходные баллы")
async def passing_scores(message: Message, state: FSMContext):
    await message.answer("Выберите направление подготовки", reply_markup=btn.choose_level)

    await state.set_state(PositionState.set_pressed_btn)
    async with state.proxy() as data:
        data["page"] = "pass_score"
    await PositionState.next()


@dp.message_handler(text="Количество мест")  # item id = 3
async def num_of_places(message: Message, state: FSMContext):
    await message.answer("Выберите направление подготовки", reply_markup=btn.choose_level)

    await state.set_state(PositionState.set_pressed_btn)
    async with state.proxy() as data:
        data["page"] = "number_of_places"
    await PositionState.next()


@dp.message_handler(text="Индивидуальные достижения")
async def achievements(message: Message):
    await message.answer(await AdmissionData.achievements())


@dp.message_handler(text="Особые права и льготы")
async def special_rights(message: Message):
    await message.answer(await AdmissionData.special_rights())


@dp.message_handler(text="Статистика приёма")
async def admission_statistics(message: Message):
    await message.answer(await AdmissionData.admiss_stat())


@dp.message_handler(text="Порядок зачисления")
async def enrollment_procedure(message: Message):
    await message.answer(await AdmissionData.enrollment_procedure())

# ---------------------------
