from aiogram import Dispatcher
from aiogram.types import BotCommand


async def setup_commands(dp: Dispatcher):
    commands = [
        BotCommand("start", "Запуск бота"),
        BotCommand("help", "Информация о боте"),
        BotCommand("exit", "Выход из режима ввода данных")
    ]
    await dp.bot.set_my_commands(commands)
