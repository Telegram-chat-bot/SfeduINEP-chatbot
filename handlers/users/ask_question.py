import logging

from loader import dp, pressed_button, bot
from aiogram.types import Message, ChatMemberStatus

from aiogram.dispatcher import FSMContext
from states.state_machine import AdminState, User_State

from utils.db_api.db_commands import get_faq, get_chat_id_group

from datetime import datetime
import re


from keyboards.inline import buttons as btn


#РАЗДЕЛ ЗАДАТЬ ВОПРОС
@dp.message_handler(text = "F.A.Q")
async def answers(message: Message):
    await message.answer(await get_faq())

@dp.message_handler(text = "Вопросы по поступлению")
async def admission_questions(message: Message):
    await message.answer("Задайте свой вопрос в диалоге. Он будет направлен представителю приёмной комиссии, который ответит Вам, как только сможет")
    await User_State.question.set()


@dp.message_handler(text = "Вопросы по направлению подготовки")
async def direction_training_questions(message: Message):
    pressed_button.append("question_direct")
    await message.answer("Задайте свой вопрос в диалоге. Он будет направлен руководителю направления подготовки, который ответит Вам, как только сможет", reply_markup=btn.choose_level)

#-----------------------------------


#СТЭЙТЫ-----------------------------
#Формирование вопроса по поступлению
@dp.message_handler(state=User_State.question)
async def question_handler(message: Message, state: FSMContext):
    await state.update_data(admission_quest = message.text)
    data: dict= await state.get_data()

    await bot.send_message(chat_id="-1001669226951", text=f"""
{datetime.now().strftime("%d.%m.%Y %H:%M")}
Вопрос от <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name} {message.from_user.last_name}</a>
Его id {message.from_user.id}

"{data.get('admission_quest')}"
    """
    )
    await message.answer("Ваш вопрос был учитан и отправлен приёмной комиссии. Ожидайте ответа")
    await state.finish()
    
@dp.message_handler(state=User_State.question_direction)
async def handler(message: Message, state: FSMContext):
    question = message.text
    
    await state.set_state(User_State.direction)
    
    try:
        direction = await state.get_data()
        
        choosed_direction = direction.get("direction")
        # choosed_level = direction.get("level")
        
        chat_id = await get_chat_id_group(choosed_direction)
        
        # if choosed_level == "bak":
        #     chat_id = "-641573369"
        # elif choosed_level == "mag":
        #     chat_id = "-749894176"
        # elif choosed_level == "spec":
        #     chat_id = "-763696760"
            
        await bot.send_message(chat_id=chat_id, text=
            f"""
{datetime.now().strftime("%d.%m.%Y %H:%M")}
Вопрос от <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name} {message.from_user.last_name}</a> по направлению {choosed_direction}
Его id: <b>{message.from_user.id}</b>

"{question}"
    """
    )
        await message.answer("Ваш вопрос был учитан и отправлен руководителю направления. Ожидайте ответа")
    except:
        await message.answer("Группа по этому направлению еще не создана или не занесена в базу данных")
        
    await state.finish()

    
@dp.message_handler(state=AdminState.get_id)
async def get_user_id(message: Message, state: FSMContext):
    await state.update_data(user_id = message.text)
    await message.answer("Напишите свой ответ")
    
    await AdminState.get_answer.set()
    
@dp.message_handler(state=AdminState.get_answer)
async def send_answer(message: Message, state: FSMContext):
    await state.update_data(answer = message.text)
    
    data = await state.get_data()
    
    await bot.send_message(
        chat_id=data.get("user_id"),
        text=f"""
Вам пришел ответ на ваш ранее заданный вопрос
"{data.get("answer")}"
        """
    )
    await message.answer("Вопрос отправлен абитуриенту")
    await state.finish()