from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from data import config
import logging

# * инициализатор бота
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# * создание хранилища для машины состояния
storage = MemoryStorage()

DEBUG: bool = True
dp = Dispatcher(bot, storage=storage)


# * обработчик для команды выхода из состояния пользовательского ввода
@dp.message_handler(Command("exit"), state="*")
async def exit_input_mode(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Ввод текста отменён")


# * Функция вывода ошибок в обработчиках исключений
def debug(error):
    if DEBUG:
        return error


filename = "" if DEBUG else "bot.log"

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO, filename=filename)
