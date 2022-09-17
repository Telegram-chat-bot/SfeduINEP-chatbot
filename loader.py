from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


# ! Задать переменной False при выгрузке в продакшн
DEBUG: bool = True
# * инициализатор бота
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# * создание хранилища для машины состояния
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
