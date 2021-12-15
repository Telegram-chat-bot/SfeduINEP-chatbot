import logging

from aiogram.dispatcher.storage import FSMContext

from loader import dp, pressed_button, bot
from aiogram.types import Message, CallbackQuery

from keyboards.inline import buttons as btn
from keyboards.inline import group_buttons as groupbtn
from states.state_machine import AdminState, PositionState
from utils.db_api import db_commands


# КОМАНДА ОТВЕТА АБИТУРИЕНТУ
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


@dp.message_handler(state=AdminState.get_id)
async def get_user_id(message: Message, state: FSMContext):
    await state.update_data(user_id=message.text)
    await message.answer("Напишите свой ответ")

    await AdminState.get_answer.set()


@dp.message_handler(state=AdminState.get_answer)
async def send_answer(message: Message, state: FSMContext):
    if message.text != "Назад" or message.text.startswith("/"):
        await state.update_data(answer=message.text)

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


@dp.message_handler(commands="add_group")
async def add_group(message: Message):
    pressed_button.append("type_group")
    await message.answer("Какого типа ваша группа?", reply_markup=groupbtn.group_type)


@dp.callback_query_handler(lambda call: call.data in ["adm_type", "dp_type"])
async def type_of_group(call: CallbackQuery, state: FSMContext):
    if call.data == "adm_type" and db_commands.ChatIDAdmission.objects.count == 0:
        try:
            await db_commands.save_chat_id_group_admission(call.message.chat.id)
            await call.message.answer("Группа успешно занесена в базу данных")
        except Exception:
            await call.message.answer("Группа уже занесена в базу данных")

    elif call.data == "dp_type":
        await call.message.answer("Выберите уровень подготовки", reply_markup=btn.choose_level)

        await state.set_state(PositionState.set_pressed_btn)
        async with state.proxy() as data:
            data["page"] = "add_group_data"
        await PositionState.next()

    else:
        await call.message.edit_text("ID чата уже есть в базе данных")
