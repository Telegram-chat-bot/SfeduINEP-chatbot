import logging
from aiogram.dispatcher.filters.builtin import AdminFilter, Text
from aiogram.dispatcher import FSMContext
from django.db.models import QuerySet

from django_admin.service.models import Users
from filters import IsGroup
from loader import dp, bot
from aiogram.types import Message, CallbackQuery

from keyboards.inline import buttons as btn
from keyboards.inline import group_buttons as group_btn

from states.state_machine import PositionState, Questions
from states.state_machine import GroupState

from utils.db_api import db_commands

from django.core.exceptions import ObjectDoesNotExist

# -----------------------------
from utils.db_api.db_commands import Database


@dp.message_handler(IsGroup(), AdminFilter(), text="Сделать объявление абитуриентам")
async def attention_message(message: Message):
    await message.answer("Напишите сообщение")
    await GroupState.attention_message.set()


# Кнопка создания объявлений пользователям
@dp.message_handler(state=GroupState.attention_message)
async def send_attention_msg(message: Message, state: FSMContext):
    announcement = message.text
    users: QuerySet = await Database(Users).get_collection_data("user_id", get_all=True)
    if len(users) > 0:
        for user in users:
            try:
                await bot.send_message(
                    chat_id=user[0],
                    text=f"""
    ❗❗❗ВНИМАНИЕ❗❗❗
    СООБЩЕНИЕ ОТ <u>АДМИНИСТРАТОРА</u>  
            
    {announcement}  
    """
                )
            except:
                continue

        await message.answer("Сообщение разослано всем пользователям")
        await state.finish()
    else:
        await message.answer("Еще никто не активировал бота. Некому рассылать")


# Обработчик кнопки удаления группы из базы данных
@dp.message_handler(IsGroup(), AdminFilter(), Text(equals="Удалить группу из базы данных"))
async def del_chat(message: Message):
    try:
        await db_commands.del_chat_id(message.chat.id)
        await message.answer("Группа удалена из базы данных")
    except ObjectDoesNotExist as error:
        await message.answer("Группа уже удалена из базы данных или не состоит в ней вовсе")
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
    # При нажатии на кнопку "Ответить" удаляется инлайн кнопка, прикрепленная к вопросу и бот предлагает ответить на
    # вопрос
    await state.set_state(Questions.answer)
    callback_data = group_btn.answer_to_question.parse(call.data)
    abiturient_question = call.message.text.split("\n")[-1]

    await call.message.delete_reply_markup()

    async with state.proxy() as data:
        data["questioner_id"] = callback_data["user_id"]
        data["question"] = abiturient_question

    await call.message.answer("Напишите ответ")
    await Questions.get_answer.set()


# Обработчик отправки сообщения с ответом
@dp.message_handler(state=Questions.get_answer)
async def send_answer(message: Message, state: FSMContext):
    user_data = await state.get_data()
    answer = message.text

    await bot.send_message(chat_id=user_data["questioner_id"], text=
    f"""
Вам пришел ответ на ваш раннее заданный вопрос:
{user_data["question"]}

<i>Ответ:</i> "{answer}"
"""
                           )
    await message.answer("Ответ был отправлен абитуриенту")
    await state.finish()


# ----------------------------------

# -----------------------------------
@dp.message_handler(IsGroup(), text="Помощь")
async def help_button(message: Message):
    await message.answer(
        await db_commands.get_help_text(chat_type=message.chat.type)
    )
# -------------------------------------
