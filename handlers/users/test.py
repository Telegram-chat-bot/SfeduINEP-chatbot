import logging
from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp, bot
from aiogram.types import Message, CallbackQuery, PollAnswer, Poll, message

from keyboards.inline import buttons as btn

from aiogram.dispatcher import FSMContext

from utils.db_api import db_commands

import asyncio


#ПАМАГИТЕ У МЕНЯ НЕ ПОЛУЧАЕТСЯ! Syntax Error с башкой
# current_direction = []
# current_question = [0]

# loop = asyncio.get_event_loop()

# # dir_code = loop.run_until_complete(db_commands.get_dir_code())

# # current_direction.append(dir_code[0].get("direction"))
# # score = {code.get("direction"): 0 for code in dir_code}

# proffesions = [
#     "Аналитик",
#     "Разработчик ГИС систем",
#     "Геоинформатик",
#     "Инженер-конструктор",
#     "Инженер-технолог по производству изделий микроэлектроники",
#     "Проектировщик микро- и наноразмерных электромеханических систем",
#     "Бионик",
#     "Архитектор медицинского оборудования",
#     "Инженер приборостроения",
#     "Менеджер-эколог",
#     "Инспектор по охране природы",
#     "Специалист по безопасности",
#     "Наноинженер",
#     "Специалист по безопасности в наноиндустрии",
#     "Проектировщик наноматериалов",
#     "Кибернетик",
#     "Менеджер в области нанотехнологий"
# ]

# answers = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Yes", callback_data="y"),
#             InlineKeyboardButton(text="No", callback_data="n")
#         ]
#     ]
# )
# questions: dict = loop.run_until_complete(db_commands.get_questions())

# @dp.message_handler(text = "Тест на профориентацию")
# async def prof_test_handler(message: Message):
#     await message.answer("Выберите уровень подготовки", reply_markup=btn.levels_prof_test)


# @dp.callback_query_handler(lambda call: call.data in ["bak-spec_test", "mag_test"])
# async def choosing_level(call: CallbackQuery):
#     if call.data == "bak-spec_test":
#         await call.message.answer("ABOBA")
#     else:
#         await call.message.answer(
# """Мы верим, что какую бы профессию вы ни выбрали - вас обязательно ждет успех! Для этого, конечно же, потребуются определенные усилия с вашей стороны. Мы, в свою очередь, сделаем все для того, чтобы ваше обучение проходило максимально комфортно и продуктивно.
# """
# )
#         await bot.send_poll(
#             chat_id=call.message.chat.id,
#             options=proffesions,
#             question="Вам предложено 17 различных профессий. Необходимо выбрать те профессии, которые больше подходят и интересны именно Вам.",
#             is_anonymous=False
#         )
    
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
    
   