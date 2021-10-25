from aiogram.dispatcher.storage import FSMContext
from keyboards import default
import keyboards
from states.state_machine import User_State

from aiogram.types import CallbackQuery
from aiogram.types.message import Message

from loader import dp, bot

from keyboards.default import menu as kb
from keyboards.inline import buttons as btn


#Обработчик выбора роли--------------------
@dp.callback_query_handler(lambda call: call.data in ['ru', 'en', 'es'])
async def callback_lang(call: CallbackQuery):
    await call.message.edit_text("Кто вы?", reply_markup=btn.roles)

#Обработчики выбранных ролей-----------------
@dp.callback_query_handler(lambda call: call.data == "abtr")
async def callback_abiturient(call: CallbackQuery):
    await call.message.answer("Выберите интересующий вас пункт", reply_markup=kb.abiturient_menu)
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)


#Направления подготовки-------------
@dp.callback_query_handler(lambda call: call.data in ["bak", "spec", "mag", "back_to", "back_to_menu"])
async def prepare_direct_block(call: CallbackQuery):
    if call.data == "bak":
        await call.message.edit_text("Направления бакалаврской подготовки:", reply_markup=btn.bak_prepare_direct)
    elif call.data == "spec":
        await call.message.edit_text("Направления специалитета:", reply_markup=btn.spec_prepare_direct)
    elif call.data == "mag":
        await call.message.edit_text("Направления магистерской подготовки:", reply_markup=btn.mag_prepare_direct)
        
    elif call.data == "back_to":
        await call.message.edit_text("Выберите направление подготовки", reply_markup=btn.choose_level)

    elif call.data == "back_to_menu":
        await call.message.delete_reply_markup()
        await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)


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