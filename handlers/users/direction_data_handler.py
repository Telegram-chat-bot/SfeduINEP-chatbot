import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageTextIsEmpty
from django.db.models import QuerySet

from django_admin.bot.models import Directions, Passing_scores, Num_places
from django_admin.service.models import ChatIDDirections

from keyboards.inline.buttons import direction_button
from loader import dp, bot, debug

from utils.db_api.db_commands import Database

from states.state_machine import UserState, PositionState, Questions

from keyboards.default import enrollee_menu as kb
from keyboards.inline import buttons as btn


@dp.callback_query_handler(lambda call: call.data in ["mag", "spec", "bak"], state=PositionState.get_pressed_btn)
async def level_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    try:
        inline_buttons = await btn.gen_directions_btns(level=call.data, page=data["page"])
        await call.message.edit_text("Выберите направление подготовки", reply_markup=inline_buttons)

    except Exception as error:
        await call.message.edit_text("Время ожидания ответа истекло")
        logging.error(error)

    await state.reset_state(with_data=False)


# Удаление инлайн кнопок
@dp.callback_query_handler(lambda call: call.data == "back_to_menu", state=PositionState.get_pressed_btn)
async def delete_markup(call: CallbackQuery, state: FSMContext):
    await call.message.delete_reply_markup()

    """
    Проверка, если это раздел с информацией о направлениях - при нажатии кнопки Назад происходит привязка главной
    клавиатуры
    """
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)
    async with state.proxy() as pressed_btn:
        if pressed_btn["page"] == "inf_dir":
            await call.message.answer("Вы вернулись в главное меню", reply_markup=kb.generate_keyboard())

    await state.finish()


@dp.callback_query_handler(direction_button.filter())
async def direction_inf_handler(call: CallbackQuery, state: FSMContext):
    data: QuerySet = await Database(Directions).get_collection_data(is_dict=True)
    callback_data: dict[str, str] = direction_button.parse(call.data)

    await bot.answer_callback_query(callback_query_id=call.id)

    try:
        # Получение словаря с данными о нажатом направлении. Преобразование его из QuerySet в словарь
        chosen_direction_data = data.filter(direction=callback_data["code"]).last()

        if callback_data["page"] == "inf_dir":
            await call.message.edit_text(
                f"Всю информацию по данному направлению вы можете найти по ссылке ниже\n{chosen_direction_data['inf']}",
                reply_markup=btn.back_btn_init)

        elif callback_data["page"] == "pass_score":
            await call.message.edit_text(
                Passing_scores.objects.get(direction_id=chosen_direction_data["id"]).inf,
                reply_markup=btn.back_btn_init
            )
        elif callback_data["page"] == "number_of_places":
            await call.message.edit_text(
                # await db_commands.get_admission_num_places(id=chosen_direction_data["id"]),
                Num_places.objects.get(direction_id=chosen_direction_data["id"]).inf,
                reply_markup=btn.back_btn_init
            )
        elif callback_data["page"] == "question_for_dir":
            await state.set_state(UserState.get_info_for_question)

            # Сохранение названия направления в стейт для дальнейшей обработки
            async with state.proxy() as qdata:
                qdata["direction"] = chosen_direction_data["direction"]

            await call.message.edit_text("Задайте вопрос")
            await Questions.user_question_dir.set()

        # Обработка кнопки добавления группы в базу данных (Работает в группах)
        elif callback_data["page"] == "add_group_data":

            ChatIDDirections(
                chat_id=call.message.chat.id,
                chat_direction=Directions.objects.get(direction=callback_data["code"])
            ).save()

            await call.message.edit_text("Группа успешно занесена в базу данных")

    except MessageTextIsEmpty:
        await call.message.edit_text("В базе данных нет информации по данному направлению",
                                     reply_markup=btn.back_btn_init)
    except Exception as error:
        await call.message.edit_text(f"Произошла ошибка:\n{debug(error)}", reply_markup=btn.back_btn_init, parse_mode="")
        logging.error(error)
