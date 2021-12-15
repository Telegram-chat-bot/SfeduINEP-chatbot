from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from django_admin.bot.models import Directions
from keyboards.inline.buttons import direction_button
from loader import dp, bot, pressed_button
from utils.db_api import db_commands
from states.state_machine import User_State, PositionState

from keyboards.inline import buttons as btn


@dp.callback_query_handler(lambda call: call.data in ["mag", "spec", "bak"], state=PositionState.get_pressed_btn)
async def level_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    try:
        keyboard = await btn.gen_directions_btns(level=call.data, page=data["page"])
        await call.message.edit_text("Выберите направление подготовки", reply_markup=keyboard)
    except Exception:
        await call.message.edit_text("Время ожидания ответа истекло")

    await state.reset_state(with_data=False)
    # await state.finish()


# Удаление инлайн кнопок
@dp.callback_query_handler(lambda call: call.data == "back_to_menu", state=PositionState.get_pressed_btn)
async def g(call: CallbackQuery, state: FSMContext):
    if call.data == "back_to_menu":
        await call.message.delete_reply_markup()
        await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)
    await state.finish()


@dp.callback_query_handler(direction_button.filter())
async def direction_inf_handler(call: CallbackQuery, state: FSMContext):
    data: dict = await db_commands.get_directions()
    callback_data: dict[str, str] = direction_button.parse(call.data)

    pressed_button.append(callback_data["page"])
    await bot.answer_callback_query(callback_query_id=call.id)
    try:
        for el in data:
            if el["direction"] == callback_data["code"]:
                # Если нет информации в бд, вызываем исключение
                if len(el["inf"]) == 0:
                    raise Exception

                if callback_data["page"] == "inf_dir":
                    await call.message.edit_text(
                        f"Всю информацию по данному направлению вы можете найти по ссылке ниже\n{el['inf']}",
                        reply_markup=btn.back_btn_init)

                elif callback_data["page"] == "pass_score":
                    await call.message.edit_text(
                        await db_commands.get_admission_passing_scores(id=el["id"]),
                        reply_markup=btn.back_btn_init
                    )
                elif callback_data["page"] == "number_of_places":
                    await call.message.edit_text(
                        await db_commands.get_admission_num_places(id=el["id"]),
                        reply_markup=btn.back_btn_init
                    )
                elif callback_data["page"] == "question_for_dir":
                    await state.set_state(User_State.get_info_for_question)

                    async with state.proxy() as qdata:
                        qdata["direction"] = el["direction"]
                    await call.message.edit_text("Задайте вопрос")

                    await User_State.user_question_dir.set()

                elif callback_data["page"] == "add_group_data":
                    await db_commands.save_chat_id_group_direction(
                        group_id = call.message.chat.id,
                        direction=Directions.objects.get(direction=callback_data["code"])
                    )

    except Exception as error:
        await call.message.edit_text(error, reply_markup=btn.back_btn_init, parse_mode="")
