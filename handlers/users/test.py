from loader import dp
from aiogram.types import Message

from keyboards.default import enrollee_menu as kb
from utils.db_api import db_commands

from aiogram.utils.exceptions import MessageTextIsEmpty
from utils import google_sheets


@dp.message_handler(text="Тест на профориентацию")
async def prof_test_handler(message: Message):
    user_id = message.from_user.id
    await message.answer(
        f""" Вы сомневаетесь в выборе подходящего направления? Не знаете что вам наиболее всего подходит? Тогда 
пройдите профориентационный тест, который был разработан нашими коллегами из психологического факультета 
специально для таких случаев. 

Собственно, сам <a href="https://docs.google.com/forms/d/e/1FAIpQLSeNkbEzcvxl7JsUxuYu13ECBLlZZrxJNyBjC_krgnZbVrUcjQ/viewform?usp=pp_url&entry.834901947={user_id}">профориентационный тест</a> """,
        reply_markup=kb.check_results_btn
    )


@dp.message_handler(text="Получить результаты")
async def get_results(message: Message):
    await message.answer("Ваш запрос обрабатывается. Подождите несколько секунд")

    query: dict = await db_commands.get_bak_directions()
    directions = dict(sorted(query.items(), key=lambda k: k[0]))

    result = await google_sheets.proftest_results.get_results(str(message.from_user.id), directions)
    try:
        await message.answer(result)

    except MessageTextIsEmpty:
        await message.answer("Вы еще не прошли профориентационный тест")
