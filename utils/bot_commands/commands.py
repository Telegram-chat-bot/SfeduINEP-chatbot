from aiogram import Dispatcher
from aiogram.types import BotCommand

commands = {
    "start": "Запуск бота",
    "help": "Информация о боте",
    "exit": "Выход из режима ввода данных"
}


async def setup_commands(dp: Dispatcher):
    array = [BotCommand(cmd, desc) for cmd, desc in commands.items()]
    await dp.bot.set_my_commands(array)
