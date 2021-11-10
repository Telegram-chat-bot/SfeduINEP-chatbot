from loader import dp, bot, item
from aiogram.types import Message

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn

#СТАРТОВОЕ СООБЩЕНИЕ
@dp.message_handler(commands="start")
async def welcome(message: Message):
    await message.answer("""
    Здравствуйте! Вас приветствует чат-бот ИНЭП ЮФУ, готов ответить на ВСЕ Ваши вопросы (но это не точно). Выберите интересующий раздел меню или задайте вопрос в диалоге.
    """, reply_markup=kb.abiturient_menu
    )
    

#ГЛАВНОЕ МЕНЮ АБИТУРИЕНТ--------------
@dp.message_handler(lambda message: message.text == "Тест на профориентацию")
async def test_prof(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Направления подготовки") #item id = 1
async def prepare_direction_item(message: Message):
    item.append("d1")
    await message.answer("Выберите специальность", reply_markup=btn.choose_level)
    

@dp.message_handler(lambda message: message.text == "Поступление")
async def admission_item(message:  Message):
    await message.answer("Все о поступлении", reply_markup=kb.university_admission)

@dp.message_handler(lambda message: message.text == "Об институте")
async def about_item(message: Message):
    await message.answer("Об институте", reply_markup=kb.about_university)

@dp.message_handler(lambda message: message.text == "Задать вопрос")
async def ask_item(message:Message):
    await message.answer("Задать вопрос",reply_markup=kb.ask_question)

#-----------------------------------------

@dp.message_handler(lambda message: message.text =="Назад")
async def back_to_btn_handler(message: Message):
    await message.answer("Вы вернулись назад", reply_markup=kb.abiturient_menu)