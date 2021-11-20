import logging

from loader import dp, pressed_button, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from utils.db_api.db_commands import get_faq

from datetime import datetime

from states.state_machine import User_State

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
    # await User_State.question.set()

#-----------------------------------

#Callback---------------------------

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
    await message.answer("Ваш вопрос был учитан и отправлен приёмной комиссии. Ожидайте ответа")
    await state.finish()
    
@dp.message_handler(state=User_State.question_direction)
async def handler(message: Message, state: FSMContext):
    question = message.text
    
    await state.set_state(User_State.direction)
    
    direction = await state.get_data()
    chat_id = ""
    
    if direction["choosed_direction"]["level"] == "bak":
        chat_id = "-641573369"
    elif direction["choosed_direction"]["level"] == "mag":
        chat_id = "-749894176"
    elif direction["choosed_direction"]["level"] == "spec":
        chat_id = "-763696760"
        
    await bot.send_message(chat_id=chat_id, text=f"""
{datetime.now().strftime("%d.%m.%Y %H:%M")}
Вопрос от <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name} {message.from_user.last_name}</a> по направлению {direction["choosed_direction"]["direction"]}

"{question}"
"""
)
    await state.finish()