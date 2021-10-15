from loader import dp, bot
from aiogram.types import Message, CallbackQuery

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn


@dp.message_handler(commands="start")
async def welcome(message: Message):
    await message.answer("Привет, выбери язык|Hello, choose language|Hola, elige tu idioma", reply_markup=btn.lang_key)



#Обработчики главных разделов---------------
@dp.message_handler(lambda message: message.text in kb.check)
async def prepare_direct(message: Message):
    await message.answer("Выберите интересующий вас уровень подготовки", reply_markup=btn.choose_level)

@dp.message_handler(lambda message:message.text =="Об институте")
async def callback_level(message:Message):
    await message.answer("Временная заглушка",reply_markup=kb.about_university)

@dp.message_handler(lambda message:message.text =="Поступление")
async def callback_level(message:Message):
    await message.answer("Временная заглушка",reply_markup=kb.university_admission)

@dp.message_handler(lambda message:message.text =="Задать вопрос")
async def callback_level(message:Message):
    await message.answer("Временная заглушка",reply_markup=kb.ask_question)

@dp.message_handler(lambda message:message.text =="Назад")
async def callback_level(message:Message):
    await message.answer("Вы вернулись назад",reply_markup=kb.abiturient_menu)




#тест на профореинтацию-->
#@dp.message_handler(lambda message:message.text == "Тест на профориентацию")
#async def callback_level(message:Message):
 #   pass






#направления подготовки --> бакалавр\магистр --> статья с ссылкой бак\маг
@dp.message_handler(lambda message:message.text == "Направления подготовки")
async def napravlenia(message:Message):
    await message.answer("1 октября будет доступно",reply_markup = btn.choose_level)
    @dp.callback_query_handler(lambda call:call.data =="mag")
    async def test(call:CallbackQuery):
        await message.answer("1 октября будет известны направления для магистров",reply_markup = btn.train_mag)
    @dp.callback_query_handler(lambda call:call.data =="bak")
    async def test(call:CallbackQuery):
        await message.answer("1 октября будет известны направления для бакалавриата ",reply_markup = btn.train_bak)





#вступительные испытания --> бакалавр\магистр --> статья с ссылкой бак\маг
@dp.message_handler(lambda message:message.text == "Вступительные испытания")
async def napravlenia(message:Message):
    await message.answer("1 октября будет доступно",reply_markup = btn.choose_level)
    @dp.callback_query_handler(lambda call: call.data == "mag")
    async def text(call: CallbackQuery):
        await message.answer("1 октября будет все известны испытания для магов",reply_markup = btn.challengs_mag) #train_mag надо изменить
    @dp.callback_query_handler(lambda call: call.data == "bak")
    async def text(call: CallbackQuery):
        await message.answer("1 октября будет все известны испытания для бАкара",reply_markup = btn.challengs_bak) #train_bak надо изменить




#поступление-->правила приема-->статья с ссылкой бак
@dp.message_handler(lambda message:message.text == "Правила приема")
async def pravila_url(message:Message):
    await message.answer("С правилами приема можете ознакомиться ниже",reply_markup = btn.choose_level)
    @dp.callback_query_handler(lambda call:call.data =="mag")
    async def test(call:CallbackQuery):
        await message.answer("1 октября будет известны направления для магистров",reply_markup = btn.rules)#поменять rules
    @dp.callback_query_handler(lambda call:call.data =="bak")
    async def test(call:CallbackQuery):
        await message.answer("1 октября будет известны направления для бакалавриата ",reply_markup = btn.rules)#поменять rules




#поступление-->подать документы-->
#поступление-->проходные баллы-->
#поступление-->количество мест-->
#поступление-->индивидуальные достижения-->https://sfedu.ru/www/stat_pages22.show?p=ABT/N8202/P#s6
#поступление-->особые права и льготы-->https://sfedu.ru/www/stat_pages22.show?p=ABT/N8202/P#s7
#поступление-->статистика приема-->https://sfedu.ru/www/stat_pages22.show?p=ABT/N8201/P
#поступление-->порядок зачисления-->https://inep.sfedu.ru/postuplenie/enter-university/    (описание простым языком с этой ссылкой)




#об университете-->записаться на экскурсию-->
#об университете-->наука и учеба-->
#об университете-->мероприятия-->
#об университете-->спорт и куультура-->
#об университете-->конкурсы-->https://inep.sfedu.ru/category/comp_stud/
#об университете-->партнеры и трудоустройство-->https://inep.sfedu.ru/partners/    ||  https://inep.sfedu.ru/job/
#об университете-->новости-->https://inep.sfedu.ru/category/news/
#об университете-->общежитие и столовые-->
#об университете-->фото-->
#об университете-->контакты-->
                       # Балакирев Сергей Вячеславович +7-928-181-93-90 sbalakirev@sfedu.ru 
                       # Житяев Игорь Леонидович +7-908-518-87-56 izhityaev@sfedu.ru 




#задать вопрос-->F.A.Q-->
#задать вопрос-->Вопросы по поступлению-->
#задать вопрос-->Вопросы по направлению подготовки-->












