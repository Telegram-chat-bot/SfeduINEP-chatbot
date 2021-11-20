import logging
from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp, bot
from aiogram.types import Message, CallbackQuery, PollAnswer, Poll, message

from aiogram.dispatcher import FSMContext
from states.state_machine import TestState
from utils.db_api import db_commands

import asyncio
# loop = asyncio.get_event_loop()

# d = loop.run_until_complete(db_commands.get_directions())
# dirs = [i["direction"] for i in d]
# logging.info(dirs)

# questions = loop.run_until_complete(db_commands.get_questions())

current_question = [0]

directions = [
    "21.03.02",
    "11.03.04",
    "12.03.01"
    # "12.03.04",
    # "20.03.01",
    # "28.03.02",
    # "26.05.04"
]
score = {
    "21.03.02": 0,
    "11.03.04": 0,
    "12.03.01": 0
}
questions = {
        "21.03.02": [
        """Хотели ли бы Вы научиться проводить измерения земельных участков с помощью 
специального оборудования и разделять их на определенные зоны?""",

        "Хотели ли бы Вы заниматься благоустройством городов и других жилых территорий?",
        
        "Хотели ли бы Вы научиться составлять карты местностей?"],
        
        "11.03.04": [
            "Хотите ли Вы научиться проектировать электронные и оптические приборы?",
            "Хотите ли Вы создавать материалы и структуры для аппаратных систем искусственного интеллекта?",
            "Интересуют ли Вас электрические цепи и схемы?"
            ],
        "12.03.01": [
            "Хотите ли Вы узнать, как устроены и проектируются приборы и технические системы?",
            "Интересно ли Вам узнавать, какие существуют методы определения качества?",
            "Хотите ли Вы побольше узнать об акустике?"
        ]
    }

data = ["Да", "Нет"]

@dp.message_handler(text = "Тест на профориентацию")
async def prof_test_handler(message: Message):
    quiz = await bot.send_poll(
        chat_id=message.chat.id, 
        question=questions[directions[current_question[0]]][0],
        options=data,
        is_anonymous=False)
    
@dp.poll_answer_handler()
async def test(answer: PollAnswer):
    if data.index(data[0]) == answer.option_ids[0]:
        score[directions[current_question[0]]] += 1
        # questions[directions[current_question[0]]][-1] += 1
    for i in questions[directions[current_question[0]]]:
        await bot.send_poll(
            chat_id=answer.user.id, 
            question=i,
            options=data,
            is_anonymous=False)
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
    
   