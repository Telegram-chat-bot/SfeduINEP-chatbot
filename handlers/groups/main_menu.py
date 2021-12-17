import logging
import re

from aiogram.dispatcher import FSMContext

from filters import IsGroup
from loader import dp, bot
from aiogram.types import Message, CallbackQuery

from keyboards.inline import buttons as btn
from keyboards.inline import group_buttons as group_btn

from states.state_machine import PositionState
from states.state_machine import AdminState

from utils.db_api import db_commands


# --------------------------
@dp.message_handler(text="Ответить на вопрос")
async def answer_to_question(message: Message, state: FSMContext):
    await message.answer("Введите id человека, предоставленный в вопросе")
    await state.set_state(AdminState.get_id)


@dp.message_handler(state=AdminState.get_id)
async def get_user_id(message: Message, state: FSMContext):
    if re.compile(r"\d{9,10}").match(message.text):
        await state.update_data(user_id=message.text)
        await message.answer("Напишите свой ответ")

        await AdminState.get_answer.set()
    else:
        await message.answer("Некорректный ID. Введите заново")


@dp.message_handler(state=AdminState.get_answer)
async def send_answer(message: Message, state: FSMContext):
    # if message.text != "/reset":
    await state.update_data(answer=message.text)

    data = await state.get_data()

    await bot.send_message(
        chat_id=data.get("user_id"),
        text=f"""
Вам пришел ответ на ваш ранее заданный вопрос
"{data.get("answer")}"
        """
    )
    await message.answer("Ответ на вопрос отправлен абитуриенту")
    await state.finish()


# -----------------------------

# -----------------------------
@dp.message_handler(IsGroup(), text="Удалить группу из базы данных")
async def del_chat(message: Message):
    try:
        await db_commands.del_chat_id(message.chat.id)
        await message.answer("Группа удалена из базы данных")
    except Exception as error:
        await message.answer("Ошибка")
        logging.error(error)


# --------------------------------

# -------------------------------
@dp.message_handler(IsGroup(), text="Занести группу в базу данных")
async def add_group(message: Message):
    await message.answer("Какого типа ваша группа?", reply_markup=group_btn.group_type)


@dp.callback_query_handler(lambda call: call.data in ["adm_type", "dp_type"])
async def type_of_group(call: CallbackQuery, state: FSMContext):
    chat_exists: bool = await db_commands.isChatExist(call.message.chat.id)

    if call.data == "adm_type" and not chat_exists:  # and db_commands.ChatIDAdmission.objects.count == 0:
        try:
            await db_commands.save_chat_id_group_admission(call.message.chat.id)
            await call.message.answer("Группа успешно занесена в базу данных")
        except Exception as error:
            await call.message.edit_text(f"Группа уже занесена в базу данных", parse_mode='')
            logging.error(error)

    elif call.data == "dp_type" and not chat_exists:
        await call.message.answer("Выберите уровень подготовки", reply_markup=btn.choose_level)

        await state.set_state(PositionState.set_pressed_btn)
        async with state.proxy() as data:
            data["page"] = "add_group_data"
        await PositionState.next()

    else:
        await call.message.answer("ID группы уже существует в базе данных")


# ----------------------------------

# -----------------------------------
@dp.message_handler(IsGroup(), text="Помощь")
async def help_button(message: Message):
    await message.answer(
        """
Краткий экскурс в команды бота:
/exit - команда, которая позволяет выйти из режима ввода данных боту (отмена этого действия);
        """
    )
# -------------------------------------
