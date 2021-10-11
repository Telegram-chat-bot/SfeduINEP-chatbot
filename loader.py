from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from data import config
import logging

bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


#Логгирование
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',level=logging.INFO,)