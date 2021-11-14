import logging
from loader import dp, item, bot

from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, message

from keyboards.inline import buttons as btn
from keyboards.default import menu as kb

from utils.db_api import db_commands
from django_admin.bot.models import Directions
import asyncio


loop = asyncio.get_event_loop()

keyboard = InlineKeyboardMarkup(row_width=1).add(btn.back_btn)


@dp.callback_query_handler(lambda call: call.data in ["bak", "spec", "mag"])
async def direct_of_prepare_handler(call: CallbackQuery):
    keyboard = await btn.gen_directions_btns_bak(level=call.data)
    await call.message.edit_text("Выберите направление подготовки", reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data in [element[0] for element in Directions.objects.values_list("direction")])
async def direction_inf_handler(call: CallbackQuery):
    data = await db_commands.get_directions()
    try:
        for el in data:
            if el["direction"] == call.data:
                if item[-1] == "d1":
                    url_btn = await btn.init_url(el["inf"])
                    await call.message.edit_text("Всю информацию по данному направлению вы можете найти по ссылке ниже", reply_markup=url_btn)
                    
                elif item[-1] == "d2":
                    await call.message.edit_text(await db_commands.get_passing_scores(id = el["id"]), reply_markup=btn.back_btn_init)
                    
                elif item[-1] == "d3":
                    await call.message.edit_text(await db_commands.get_num_places(id = el["id"]), reply_markup=btn.back_btn_init)

    except Exception:
        await call.message.edit_text("По данному направлению информация отсутствует", reply_markup=btn.back_btn_init)
        await call.message.answer(Exception)
