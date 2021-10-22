from loader import dp, bot
from aiogram.types import Message
import articels

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn

#СТАРТОВОЕ СООБЩЕНИЕ
@dp.message_handler(commands="start")
async def welcome(message: Message):
    await message.answer("Привет, выбери язык|Hello, choose language|Hola, elige tu idioma", reply_markup=btn.lang_key)


#ГЛАВНОЕ МЕНЮ АБИТУРИЕНТ--------------
@dp.message_handler(lambda message: message.text == "Тест на профориентацию")
async def test_prof(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Направления подготовки")
async def prepare_direction_item(message: Message):
    await message.answer("Выберите специальность", reply_markup=btn.choose_level)

@dp.message_handler(lambda message:message.text == "Вступительные испытания")
async def napravlenia(message:Message):
    await message.answer("Выберите направление подготовки", reply_markup = btn.choose_level)

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


#РАЗДЕЛ ПОСТУПЛЕНИЕ--------
@dp.message_handler(lambda message: message.text == "Правила приема")
async def rules_admission(message: Message):
    await message.answer("С правилами приема можете ознакомиться ниже", reply_markup = btn.choose_level)

@dp.message_handler(lambda message:message.text == "Подать документы")
async def submit_doc(message: Message):
    await message.answer(text = articels.postuplenie1)

@dp.message_handler(lambda message: message.text == "Проходные баллы")
async def passing_scores(message: Message):
    await message.answer(text = articels.postuplenie2)

@dp.message_handler(lambda message: message.text == "Количество мест")
async def num_of_places(message: Message):
    await message.answer(text = articels.postuplenie3)

@dp.message_handler(lambda message: message.text == "Индивидуальные достижения")
async def achievements(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Особые права и льготы")
async def special_rights(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Статистика приема")
async def admission_statcistics(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Порядок зачисления")
async def enrollment_procedure(message: Message):
    pass

#---------------------------

#РАЗДЕЛ ОБ ИНСТИТУТЕ
@dp.message_handler(lambda message: message.text == "Записаться на экскурсию")
async def excursion(message: Message):
    await message.answer(text = articels.postuplenie4)

@dp.message_handler(lambda message: message.text == "Наука и учеба")
async def science(message: Message):
    await message.answer(text = articels.postuplenie5)

@dp.message_handler(lambda message: message.text == "Мероприятия")
async def mesta(message: Message):
    await message.answer(text = articels.postuplenie6)

@dp.message_handler(lambda message:message.text == "Спорт и культура")
async def mesta(message: Message):
    await message.answer(text = articels.postuplenie7)

@dp.message_handler(lambda message: message.text == "Конкурсы")
async def competitions(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Партнеры и трудоустройство")
async def partners_employment(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Новости")
async def news(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Общежития и столовые")
async def dormitory_eatery(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Фото")
async def photos(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Контакты")
async def mesta(message: Message):
    await message.answer(text = articels.postuplenie8)

#------------------------------------

#РАЗДЕЛ ЗАДАТЬ ВОПРОС
@dp.message_handler(lambda message: message.text == "F.A.Q")
async def mesta(message: Message):
    await message.answer(text = articels.postuplenie9)

@dp.message_handler(lambda message: message.text == "Вопросы по поступлению")
async def mesta(message: Message):
    await message.answer(text = articels.postuplenie10)

@dp.message_handler(lambda message: message.text == "Вопросы по направлению подготовки")
async def direction_training_questions(message: Message):
    pass

#-----------------------------------
@dp.message_handler(lambda message:message.text == "Правила приема")
async def pravila_url(message:Message):
    await message.answer("С правилами приема можете ознакомиться ниже",reply_markup = btn.choose_level)

@dp.message_handler(lambda message:message.text == "Подать документы")
async def podat(message:Message):
    await message.answer(text = articels.postuplenie1)

@dp.message_handler(lambda message:message.text == "Проходные баллы")
async def prohod(message:Message):
    await message.answer(text = articels.postuplenie2)

@dp.message_handler(lambda message:message.text == "Количество мест")
async def mesta(message:Message):
    await message.answer(text = articels.postuplenie3)

@dp.message_handler(lambda message:message.text == "Записаться на экскурсию")
async def mesta(message:Message):
    await message.answer(text = articels.postuplenie4)

@dp.message_handler(lambda message:message.text == "Наука и учеба")
async def mesta(message:Message):
    await message.answer(text = articels.postuplenie5)

@dp.message_handler(lambda message:message.text == "Мероприятия")
async def mesta(message:Message):
    await message.answer(text = articels.postuplenie6)

@dp.message_handler(lambda message:message.text == "Спорт и культура")
async def mesta(message:Message):
    await message.answer(text = articels.postuplenie7)

@dp.message_handler(lambda message:message.text == "Контакты")
async def mesta(message:Message):
    await message.answer(text = articels.postuplenie8)

@dp.message_handler(lambda message:message.text == "F.A.Q")
async def mesta(message:Message):
    await message.answer(text = articels.postuplenie9)

@dp.message_handler(lambda message:message.text == "Вопросы по поступлению")
async def mesta(message:Message):
    await message.answer(text = articels.postuplenie10)

