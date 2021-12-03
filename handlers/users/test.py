from loader import dp, bot
from aiogram.types import Message

from keyboards.default import menu as kb

from utils.db_api import db_commands

from aiogram.utils.exceptions import MessageTextIsEmpty
from utils.google_sheets import proftest_results



@dp.message_handler(text = "Тест на профориентацию")
async def prof_test_handler(message: Message):
    
    
    await message.answer(
f"""
<b>ОБЯЗАТЕЛЬНО К ПРОЧТЕНИЮ❗❗❗</b>
Перед прохождением теста <u>скопируйте свой ID:</u> <b>{message.from_user.id}</b>
<i>(на мобильных устройствах зажмите сообщение, а затем выделите ID повторным зажатием)</i>
Он необходим при заполнении формы. После прохождения профориентационного теста вернитесь ко мне и нажмите на кнопку <i>"Получить результаты"</i>

Собственно, сам <a href="https://docs.google.com/forms/d/e/1FAIpQLSeNkbEzcvxl7JsUxuYu13ECBLlZZrxJNyBjC_krgnZbVrUcjQ/viewform">профориентационный тест</a>
""", reply_markup=kb.check_results_btn
)
    
    
@dp.message_handler(text="Получить результаты")
async def get_results(message: Message):
    await message.answer("Ваш запрос обрабатывается. Подождите несколько секунд")
    directions = await db_commands.get_bak_directions()
    result = await proftest_results.get_results(str(message.from_user.id), directions)
    try:
        await message.answer(result)
    except MessageTextIsEmpty:
        await message.answer("Вы еще не прошли профориентационный тест")