import logging
from os import stat
from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp, bot
from aiogram.types import Message, CallbackQuery, PollAnswer, Poll, message

from aiogram.dispatcher import FSMContext
from states.state_machine import TestState
from utils.db_api import db_commands

import asyncio


#ПАМАГИТЕ У МЕНЯ НЕ ПОЛУЧАЕТСЯ! Syntax Error с башкой
current_direction = []
current_question = [0]

loop = asyncio.get_event_loop()

dir_code = loop.run_until_complete(db_commands.get_dir_code())

current_direction.append(dir_code[0].get("direction"))
score = {code.get("direction"): 0 for code in dir_code}


questions: dict = loop.run_until_complete(db_commands.get_questions())

@dp.message_handler(text = "Тест на профориентацию")
async def prof_test_handler(message: Message):

    await message.answer(
        questions[current_direction[0]][0]
    )
    await TestState.q1.set()
        
@dp.message_handler(state=TestState.q1)
async def answer_q1(message: Message, state: FSMContext):
    if message.text.lower() == "да":
        score[current_direction[0]] += 1
        await message.answer(
            questions[current_direction[0]][1]
        )
        
    elif message.text.lower != "нет":
        await message.answer("Некорректный ответ")
    
    await state.update_data(a1 = message.text)
    await TestState.next()

@dp.message_handler(state=TestState.q2)
async def answer_q2(message: Message, state: FSMContext):
    if message.text.lower() == "да":
        score[current_direction[0]] += 1
        await message.answer(
            questions[current_direction[0]][2]
        )
        
    elif message.text.lower != "нет":
        await message.answer("Некорректный ответ")
        
    await state.update_data(a2=message.text)
    data = await state.get_data()
    await message.answer(f"{data.get('a1')}\n{data.get('a2')}\n{score}")
# @dp.poll_answer_handler()
# async def test(answer: PollAnswer):
#     if data.index(data[0]) == answer.option_ids[0]:
#         score[directions[current_question[0]]] += 1
        

#     if current_question[0] < len(directions) + 1:
#         await bot.send_poll(
#             chat_id=answer.user.id, 
#             question=questions[directions[current_question[0]]][current_question[0]],
#             options=data,
#             is_anonymous=False)
        
#     current_question[0] += 1
    # kolvo = len(questions[directions[current_question[0]]])
    # current_question[0] += 1

    # if current_question[0] != 9:
    #     if kolvo > 2:
    #         await bot.send_poll(
    #             chat_id=answer.user.id, 
    #             question=questions[directions[current_question[0]-1]][current_question[0]],
    #             options=data,
    #             is_anonymous=False)
    #     else:
    #         await bot.send_poll(
    #             chat_id=answer.user.id, 
    #             question=questions[directions[current_question[0]]][current_question[0]],
    #             options=data,
    #             is_anonymous=False)
    
   