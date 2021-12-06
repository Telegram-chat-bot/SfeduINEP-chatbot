import logging

from aiogram.types import CallbackQuery
from aiogram.dispatcher.storage import FSMContext

from states.state_machine import User_State

from loader import dp, pressed_button

from keyboards.inline import buttons as btn

from utils.db_api import db_commands
from django_admin.bot.models import Directions


@dp.callback_query_handler(lambda call: call.data in ["bak", "spec", "mag"])
async def direct_of_prepare_handler(call: CallbackQuery):
    keyboard = await btn.gen_directions_btns_bak(level=call.data)
    await call.message.edit_text("Выберите направление подготовки", reply_markup=keyboard)
    
@dp.message_handler(state=User_State.direction)
@dp.callback_query_handler(lambda call: call.data in [element[0] for element in Directions.objects.values_list("direction")])
async def direction_inf_handler(call: CallbackQuery, state: FSMContext):
    data: dict = await db_commands.get_directions()
    try:
        for el in data:
            if el["direction"] == call.data:
                #Если нет информации в бд, вызываем исключение
                if len(el["inf"]) == 0:
                    raise Exception
                
                #Если была нажата кнопка Направления подготовки
                if pressed_button[-1] == "dir_inf":
                    await call.message.edit_text(
                        f"Всю информацию по данному направлению вы можете найти по ссылке ниже\n{el['inf']}", 
                        reply_markup=btn.back_btn_init
                        )
                    
                #Если была нажата кнопка Проходные баллы
                elif pressed_button[-1] == "dir_pass":
                    await call.message.edit_text(
                        await db_commands.get_admission_passing_scores(id = el["id"]),
                        reply_markup=btn.back_btn_init
                        )
                    
                #Если была нажата кнопка Количество мест   
                elif pressed_button[-1] == "num_places":
                    await call.message.edit_text(
                        await db_commands.get_admission_num_places(id = el["id"]), 
                        reply_markup=btn.back_btn_init
                        )
                    
                #Если была нажата кнопка Вопрос по направлению подготовки
                elif pressed_button[-1] == "question_direct":
                    async with state.proxy() as qdata:
                        qdata["direction"] = el["direction"]
                    
                    await call.message.edit_text("Задайте вопрос")
                    await User_State.question_direction.set()

    except Exception:
        await call.message.edit_text("По данному направлению информация отсутствует", reply_markup=btn.back_btn_init)
