import logging
from aiogram.dispatcher.filters.builtin import AdminFilter, Text
from aiogram.dispatcher import FSMContext
from django.db.models import QuerySet

from filters import IsGroup
from loader import dp, bot
from aiogram.types import Message, CallbackQuery

from keyboards.inline import buttons as btn
from keyboards.inline import group_buttons as group_btn

from states.state_machine import PositionState, Questions
from states.state_machine import GroupState

from utils.db_api import db_commands


# -----------------------------
@dp.message_handler(IsGroup(), AdminFilter(), text="Сделать объявление абитуриентам")
async def attention_message(message: Message):
    await message.answer("Напишите сообщение")
    await GroupState.attention_message.set()


@dp.message_handler(state=GroupState.attention_message)
async def send_attention_msg(message: Message, state: FSMContext):
    message_to = message.text
    users: QuerySet = await db_commands.get_users()

    for user in users:
        try:
            await bot.send_message(
                chat_id=user[0],
                text=f"""
❗❗❗ВНИМАНИЕ❗❗❗
СООБЩЕНИЕ ОТ <u>АДМИНИСТРАТОРА</u>  
        
{message_to}  
"""
        )
        except:
            continue

    await message.answer("Сообщение разослано всем пользователям")
    await state.finish()


@dp.message_handler(IsGroup(), AdminFilter(), Text(equals="Удалить группу из базы данных"))
async def del_chat(message: Message):
    try:
        await db_commands.del_chat_id(message.chat.id)
        await message.answer("Группа удалена из базы данных")
    except Exception as error:
        await message.answer("Группа уже удалена из базы данных")
        logging.error(error)


# --------------------------------

# -------------------------------
@dp.message_handler(IsGroup(), AdminFilter(), text="Занести группу в базу данных")
async def add_group(message: Message):
    await message.answer("Какого типа ваша группа?", reply_markup=group_btn.group_type)


@dp.callback_query_handler(lambda call: call.data in ["adm_type", "dp_type"])
async def type_of_group(call: CallbackQuery, state: FSMContext):
    chat_exists: bool = await db_commands.isChatExist(call.message.chat.id)

    if call.data == "adm_type" and not chat_exists:
        try:
            await db_commands.save_chat_id_group_admission(call.message.chat.id)
            await call.message.edit_text("Группа успешно занесена в базу данных")
        except Exception as error:
            await call.message.edit_text(f"Группа уже занесена в базу данных", parse_mode='')
            logging.error(error)

    elif call.data == "dp_type" and not chat_exists:
        await call.message.edit_text("Выберите уровень подготовки", reply_markup=btn.choose_level)

        await state.set_state(PositionState.set_pressed_btn)
        async with state.proxy() as data:
            data["page"] = "add_group_data"
        await PositionState.next()

    else:
        await call.message.edit_text("ID группы уже существует в базе данных")


# Обработчик кнопки "Ответить"
@dp.callback_query_handler(group_btn.answer_to_question.filter())
async def ask_to_question_handler(call: CallbackQuery, state: FSMContext):
    await state.set_state(Questions.answer)
    callback_data = group_btn.answer_to_question.parse(call.data)
    await call.message.delete_reply_markup()

    async with state.proxy() as data:
        data["questioner_id"] = callback_data["user_id"]

    await call.message.answer("Напишите ответ")
    await Questions.get_answer.set()


# Обработчик отправки сообщения с ответом
@dp.message_handler(state=Questions.get_answer)
async def send_answer(message: Message, state: FSMContext):
    user_id = await state.get_data()
    answer = message.text

    await bot.send_message(chat_id=user_id["questioner_id"], text=
    f"""
Вам пришел ответ на ваш раннее заданный вопрос

"{answer}"
"""
                           )
    await message.answer("Ответ был отправлен абитуриенту")
    await state.finish()


# ----------------------------------

# -----------------------------------
@dp.message_handler(IsGroup(), text="Помощь")
async def help_button(message: Message):
    await message.answer(
        """Краткий экскурс в команды бота: /exit - команда, которая позволяет выйти из режима ввода данных боту ( 
отмена этого действия);

<b>Ответ на вопрос</b>
Чтобы ответить абитуриенту, необходимо:
1) Нажать на кнопку <i>"Ответить на вопрос"</i>;
2) Ввести <b>ID</b> абитуриента, который указан в вопросе;
3) Ввести свой ответ и отправить.

<b>P.S.</b>
<i>Чтобы скопировать конкретный участок текста сообщения 
на мобильных устройствах, необходимо зажать сообщение -> зажать нужный фрагмент текста и скопировать )</i> """
    )
# -------------------------------------
