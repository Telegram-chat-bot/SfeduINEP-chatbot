from loader import dp, bot, item
from aiogram.types import Message
import articels

from states.state_machine import User_State
from aiogram.dispatcher import FSMContext

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

@dp.message_handler(lambda message: message.text == "Направления подготовки") #item id = 1
async def prepare_direction_item(message: Message):
    item.insert(0, 1)
    await message.answer("Выберите специальность", reply_markup=btn.choose_level)

@dp.message_handler(lambda message:message.text == "Вступительные испытания") #item id = 2
async def passing_scores_item(message:Message):
    item.insert(0, 2)
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
    await message.answer(text=articels.rules_admission_article)

@dp.message_handler(lambda message:message.text == "Подать документы")
async def submit_doc(message: Message):
    await message.answer(text = articels.submit_documents_article)

@dp.message_handler(lambda message: message.text == "Проходные баллы")
async def passing_scores(message: Message):
    await message.answer(text = articels.passing_scores_article)

@dp.message_handler(lambda message: message.text == "Количество мест")  #item id = 3
async def num_of_places(message: Message):
    item.insert(0,3)
    await message.answer("Выберите направление подготовки", reply_markup=btn.choose_level)

@dp.message_handler(lambda message: message.text == "Индивидуальные достижения")
async def achievements(message: Message):
    await message.answer(text = articels.achievements_article)

@dp.message_handler(lambda message: message.text == "Особые права и льготы")
async def special_rights(message: Message):
    await message.answer(text = articels.special_rights_article)

@dp.message_handler(lambda message: message.text == "Статистика приема")
async def admission_statcistics(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Порядок зачисления")
async def enrollment_procedure(message: Message):
    await message.answer(text = articels.enrollment_procedure_article)

#---------------------------

#РАЗДЕЛ ОБ ИНСТИТУТЕ
@dp.message_handler(lambda message: message.text == "Записаться на экскурсию")
async def excursion(message: Message):
    await message.answer(text = articels.excursion_article)

@dp.message_handler(lambda message: message.text == "Наука и учеба")
async def science(message: Message):
    await message.answer(text = articels.science_article)

@dp.message_handler(lambda message: message.text == "Мероприятия")
async def events(message: Message):
    await message.answer(text = articels.events_article)

@dp.message_handler(lambda message:message.text == "Спорт и культура")
async def sport_and_culture(message: Message):
    await message.answer(text = articels.sport_and_culture_article)

@dp.message_handler(lambda message: message.text == "Конкурсы")
async def competitions(message: Message):
    await message.answer(text = articels.competitions_article)

@dp.message_handler(lambda message: message.text == "Партнеры и трудоустройство")
async def partners_employment(message: Message):
    await message.answer(text = articels.partners_employment_article)

@dp.message_handler(lambda message: message.text == "Новости")
async def news(message: Message):
    await message.answer(text=articels.news_article)

@dp.message_handler(lambda message: message.text == "Общежития и столовые")
async def dormitory_eatery(message: Message):
    await message.answer(text = articels.dormitory_eatery_article)
    with open("img/dormitories.jpg", "rb") as photo:
        await bot.send_photo(photo=photo, chat_id=message.chat.id)

@dp.message_handler(lambda message: message.text == "Фото")
async def photos(message: Message):
    pass

@dp.message_handler(lambda message: message.text == "Контакты")
async def contacts(message: Message):
    await message.answer(text = articels.contact_article)

#------------------------------------

#РАЗДЕЛ ЗАДАТЬ ВОПРОС
@dp.message_handler(lambda message: message.text == "F.A.Q")
async def answers(message: Message):
    await message.answer(text = articels.faq_article)

@dp.message_handler(lambda message: message.text == "Вопросы по поступлению")
async def admission_questions(message: Message):
    await message.answer(text = articels.admission_question_article)

@dp.message_handler(lambda message: message.text == "Вопросы по направлению подготовки")
async def direction_training_questions(message: Message):
    pass

#-----------------------------------