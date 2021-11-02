from logging import error
from os import link
from loader import dp, bot, item, db
from aiogram.types import Message
from data import articels

from states.state_machine import User_State
from aiogram.dispatcher import FSMContext

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn

from datetime import datetime

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


#РАЗДЕЛ ПОСТУПЛЕНИЕ--------
@dp.message_handler(lambda message: message.text == "Правила приема")
async def rules_admission(message: Message):
    # await message.answer(text=articels.rules_admission_article)
    data = await db.get_data(block="admission", element="admission_rules")
    await message.answer(data[0].get("admission_rules"))

@dp.message_handler(lambda message:message.text == "Подать документы")
async def submit_doc(message: Message):
    data = await db.get_data(block="admission", element="submit_doc")
    await message.answer(data[0].get("submit_doc"))

@dp.message_handler(lambda message: message.text == "Проходные баллы")
async def passing_scores(message: Message):
    item.append("d2")
    await message.answer("Выберите направление подготовки", reply_markup = btn.choose_level)

@dp.message_handler(lambda message: message.text == "Количество мест")  #item id = 3
async def num_of_places(message: Message):
    item.append("d3")
    await message.answer("Выберите направление подготовки", reply_markup=btn.choose_level)

@dp.message_handler(lambda message: message.text == "Индивидуальные достижения")
async def achievements(message: Message):
    # await message.answer(text = articels.achievements_article)
    data = await db.get_data(block="admission", element="achievements")
    await message.answer(data[0].get("achievements"))

@dp.message_handler(lambda message: message.text == "Особые права и льготы")
async def special_rights(message: Message):
    # await message.answer(text = articels.special_rights_article)
    data = await db.get_data(block="admission", element="special_rights")
    await message.answer(data[0].get("special_rights"))

@dp.message_handler(lambda message: message.text == "Статистика приёма")
async def admission_statcistics(message: Message):
    links = [f"https://inep.sfedu.ru/statistika-za-20{y}-god/" for y in range(18, 21)]

    await message.answer("Статистику приёма за прошлые годы вы можете просмотреть по следующим ссылкам \n".join(list(set(links))))

@dp.message_handler(lambda message: message.text == "Порядок зачисления")
async def enrollment_procedure(message: Message):
    data = await db.get_data(block="admission", element="enrollment_proc")
    await message.answer(data[0].get("enrollment_proc"))
    # await message.answer(text = articels.enrollment_procedure_article)

#---------------------------

#РАЗДЕЛ ОБ ИНСТИТУТЕ
@dp.message_handler(lambda message: message.text == "Знакомство")
async def excursion(message: Message):
    # await message.answer(text = articels.acquaintance_article)
    data = await db.get_data(block="about", element="acquaintance")
    await message.answer(data[0].get("acquaintance"))

@dp.message_handler(lambda message: message.text == "Записаться на экскурсию")
async def excursion(message: Message):
    # await message.answer(text = articels.excursion_article)
    data = await db.get_data(block="about", element="excursion")
    await message.answer(data[0].get("excursion"))

@dp.message_handler(lambda message: message.text == "Наука и учёба")
async def science(message: Message):
    # await message.answer(text = articels.science_article)
    data = await db.get_data(block="about", element="science")
    await message.answer(data[0].get("science"))

@dp.message_handler(lambda message: message.text == "Мероприятия")
async def events(message: Message):
    # await message.answer(text = articels.events_article)
    data = await db.get_data(block="about", element="events")
    await message.answer(data[0].get("events"))

@dp.message_handler(lambda message: message.text == "Партнеры и трудоустройство")
async def partners_employment(message: Message):
    # await message.answer(text = articels.partners_employment_article)
    data = await db.get_data(block="about", element="partners_work")
    await message.answer(data[0].get("partners_work"))

@dp.message_handler(lambda message: message.text == "Студсовет")
async def stud_council(message: Message):
    # await message.answer(text = articels.stud_council_article)
    data = await db.get_data(block="about", element="stud_council")
    await message.answer(data[0].get("stud_council"))

@dp.message_handler(lambda message: message.text == "Карта")
async def excursion(message: Message):
    await bot.send_location(chat_id=message.chat.id, latitude="47.208399", longitude="38.936603")

@dp.message_handler(lambda message: message.text == "Фото")
async def photo(message: Message):
    # await message.answer(articels.photo_article)
    data = await db.get_data(block="about", element="photo")
    await message.answer(data[0].get("photo"))

@dp.message_handler(lambda message: message.text == "Контакты")
async def contacts(message: Message):
    # await message.answer(text = articels.contact_article)
    data = await db.get_data(block="about", element="contacts")
    await message.answer(data[0].get("contacts"))


#РАЗДЕЛ ЗАДАТЬ ВОПРОС
@dp.message_handler(lambda message: message.text == "F.A.Q")
async def answers(message: Message):
    await message.answer(text = articels.faq_article)

@dp.message_handler(lambda message: message.text == "Вопросы по поступлению")
async def admission_questions(message: Message):
    item.append("q1")
    await message.answer("Задайте свой вопрос в диалоге. Он будет направлен представителю приёмной комиссии, который ответит Вам, как только сможет")
    await User_State.question.set()


@dp.message_handler(lambda message: message.text == "Вопросы по направлению подготовки")
async def direction_training_questions(message: Message):
    item.append("q2")
    await message.answer("Задайте свой вопрос в диалоге. Он будет направлен руководителю направления подготовки, который ответит Вам, как только сможет", reply_markup=btn.choose_level)
    await User_State.question.set()

#-----------------------------------

#СТЭЙТЫ-----------------------------
@dp.message_handler(state=User_State.question)
async def question_handler(message: Message, state: FSMContext):
    await state.update_data(admission_quest = message.text)
    data = await state.get_data()

    await bot.send_message(chat_id="-783193836", text=f"""
{datetime.now().strftime("%d.%m.%Y %H:%M")}
Вопрос от <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name} {message.from_user.last_name}</a>

"{data.get('admission_quest')}"
    """
    )
    await message.answer("Ваш вопрос был учитан и отправлен приёмной комиссии. Вам напишут в личку")

    await state.finish()