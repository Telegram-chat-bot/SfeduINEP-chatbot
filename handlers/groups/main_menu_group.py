import logging
from aiogram.dispatcher.filters.builtin import AdminFilter, Text
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BotBlocked
from django.db.models import QuerySet

from django_admin.bot.models import Help_content
from django_admin.service.models import Users, ChatIDAdmission, ChatIDDirections
from filters import IsGroup
from loader import dp, bot, debugger
from aiogram.types import Message, CallbackQuery

from keyboards.inline import buttons as btn
from keyboards.inline import group_buttons as group_btn

from states.state_machine import PositionState, Questions
from states.state_machine import GroupState

from utils.db_api import db_commands

from django.core.exceptions import ObjectDoesNotExist

# -----------------------------
from utils.db_api.db_commands import Database

group_menu: list = [
    "Сделать объявление абитуриентам",
    "Помощь",
    "Занести группу в базу данных",
    "Удалить группу из базы данных"
]


# * Кнопка создания объявлений пользователям
@dp.message_handler(IsGroup(), AdminFilter(), text="Сделать объявление абитуриентам")
async def attention_message(message: Message):
    if await db_commands.isChatExist(chat_id=message.chat.id):
        await message.answer("Напишите сообщение")
        await GroupState.attention_message.set()
    else:
        await message.answer("Группа не числится в базе данных")


@dp.message_handler(state=GroupState.attention_message)
async def send_attention_msg(message: Message, state: FSMContext):
    announcement: str = message.text
    if announcement not in group_menu:
        users: QuerySet = await Database(Users).get_collection_data("user_id", is_dict=True, get_all=True)
        if len(users):
            for user in users:
                try:
                    await bot.send_message(
                        chat_id=user["user_id"],
                        text=f"❗❗❗ВНИМАНИЕ❗❗❗\nСООБЩЕНИЕ ОТ <u>АДМИНИСТРАТОРА</u>\n'{announcement}'"
                    )
                except BotBlocked:
                    continue

            await message.answer("Сообщение разослано всем пользователям")
            await state.finish()
        else:
            await message.answer("Еще никто не активировал бота. Некому рассылать")
    else:
        await message.answer("Введите сообщение или активируйте команду /exit")


# * Обработчик кнопки удаления группы из базы данных
@dp.message_handler(IsGroup(), AdminFilter(), Text(equals="Удалить группу из базы данных"))
async def del_chat(message: Message):
    try:
        await db_commands.del_chat_id(message.chat.id)
        await message.answer("Группа удалена из базы данных")

    except ObjectDoesNotExist as error:
        await message.answer(
            f"Группа уже удалена из базы данных или не состоит в ней вовсе.\n{await debugger(str(error))}"
        )
        logging.error(error)


# * Обработчик кнопки "Занести группу в базу данных"
@dp.message_handler(IsGroup(), AdminFilter(), text="Занести группу в базу данных")
async def add_group(message: Message):
    chat_exists: bool = await db_commands.isChatExist(message.chat.id)
    if not chat_exists:
        await message.answer("Какого типа ваша группа?", reply_markup=group_btn.group_type)
    else:
        await message.answer("Группа уже числится в базе данных")


# * Обработчик инлайн кнопок выбора типа группы
@dp.callback_query_handler(lambda call: call.data in ["adm_type", "dp_type"])
async def type_of_group(call: CallbackQuery, state: FSMContext):
    if call.data == "adm_type":
        try:
            ChatIDAdmission(chat_id=call.message.chat.id).save()
            await call.message.edit_text("Группа успешно занесена в базу данных")

        except Exception as error:
            await call.message.edit_text("Группа уже занесена в базу данных", parse_mode='')

            logging.error(error)
    elif call.data == "dp_type":
        await call.message.edit_text("Выберите уровень подготовки", reply_markup=btn.choose_level)

        await state.set_state(PositionState.set_pressed_btn)
        async with state.proxy() as data:
            data["page"] = "add_group_data"
        await PositionState.next()


# * Обработчик кнопки "Ответить"
@dp.callback_query_handler(group_btn.answer_to_question.filter())
async def ask_to_question_handler(call: CallbackQuery, state: FSMContext):
    """
    При нажатии на кнопку "Ответить" удаляется инлайн кнопка,
    прикрепленная к вопросу и бот предлагает ответить на вопрос
    """
    await state.set_state(Questions.answer)

    callback_data: dict = group_btn.answer_to_question.parse(call.data)
    matriculant_question: str = call.message.text.split("\n")[-1]

    await call.message.delete_reply_markup()

    async with state.proxy() as data:
        data["questioner_id"] = callback_data["user_id"]
        data["question"] = matriculant_question

    await call.message.answer("Напишите ответ")
    await Questions.get_answer.set()


# * Обработчик отправки сообщения с ответом
@dp.message_handler(state=Questions.get_answer)
async def send_answer(message: Message, state: FSMContext):
    user_data = await state.get_data()
    answer: str = message.text

    await bot.send_message(chat_id=user_data["questioner_id"], text=f"""
Вам пришел ответ на ваш раннее заданный вопрос:
{user_data["question"]}

<i>Ответ:</i> "{answer}"
"""
                           )
    await message.answer("Ответ был отправлен абитуриенту")
    await state.finish()


# * Обработчик кнопки Помощь
@dp.message_handler(IsGroup(), text="Помощь")
async def help_button(message: Message):
    content: str = Help_content.objects.filter(
        target_user=message.chat.type
    ).first().content

    await message.answer(content or "В этот раздел ещё не добавили информацию")
