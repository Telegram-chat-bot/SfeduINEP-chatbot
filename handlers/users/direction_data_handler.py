import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageTextIsEmpty
from django.db.models import QuerySet

from bot.models import Directions

from keyboards.inline.buttons import direction_button
from loader import dp, bot
from utils.db_api import db_commands
from states.state_machine import UserState, PositionState, Questions

from keyboards.inline import buttons as btn


@dp.callback_query_handler(lambda call: call.data in ["mag", "spec", "bak"], state=PositionState.get_pressed_btn)
async def level_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    try:
        keyboard = await btn.gen_directions_btns(level=call.data, page=data["page"])
        await call.message.edit_text("Выберите направление подготовки", reply_markup=keyboard)
    except Exception as error:
        await call.message.edit_text("Время ожидания ответа истекло")
        logging.error(error)

    await state.reset_state(with_data=False)


# Удаление инлайн кнопок
@dp.callback_query_handler(lambda call: call.data == "back_to_menu", state=PositionState.get_pressed_btn)
async def delete_markup(call: CallbackQuery, state: FSMContext):
    if call.data == "back_to_menu":
        await call.message.delete_reply_markup()
        await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)
    await state.finish()


@dp.callback_query_handler(direction_button.filter())
async def direction_inf_handler(call: CallbackQuery, state: FSMContext):
    data: QuerySet = await db_commands.get_directions()
    callback_data: dict[str, str] = direction_button.parse(call.data)

    await bot.answer_callback_query(callback_query_id=call.id)

    try:
        chosen_direction_data = data.filter(direction=callback_data["code"]).last()

        if callback_data["page"] == "inf_dir":
            await call.message.edit_text(
                f"Всю информацию по данному направлению вы можете найти по ссылке ниже\n{chosen_direction_data['inf']}",
                reply_markup=btn.back_btn_init)

        elif callback_data["page"] == "pass_score":
            await call.message.edit_text(
                await db_commands.get_admission_passing_scores(id=chosen_direction_data["id"]),
                reply_markup=btn.back_btn_init
            )
        elif callback_data["page"] == "number_of_places":
            await call.message.edit_text(
                await db_commands.get_admission_num_places(id=chosen_direction_data["id"]),
                reply_markup=btn.back_btn_init
            )
        elif callback_data["page"] == "question_for_dir":
            await state.set_state(UserState.get_info_for_question)

            async with state.proxy() as qdata:
                qdata["direction"] = chosen_direction_data["direction"]
            await call.message.edit_text("Задайте вопрос")

            await Questions.user_question_dir.set()

        elif callback_data["page"] == "add_group_data":
            await db_commands.save_chat_id_group_direction(
                group_id=call.message.chat.id,
                direction=Directions.objects.get(direction=callback_data["code"])
            )
            await call.message.edit_text("Группа успешно занесена в базу данных")

    except MessageTextIsEmpty:
        await call.message.edit_text("В базе данных нет информации по данному направлению",
                                     reply_markup=btn.back_btn_init)
    except Exception as error:
        await call.message.edit_text(f"Произошла ошибка", reply_markup=btn.back_btn_init, parse_mode="")
        logging.error(error)
