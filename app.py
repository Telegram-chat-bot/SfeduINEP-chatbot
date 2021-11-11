from aiogram.bot.bot import Bot
from aiogram.types import BotCommand

import handlers

from loader import bot, storage, db



async def on_shutdown(dp):
    await bot.close()
    await storage.close()

async def set_commands(bot: Bot):
    commands = [
        BotCommand("start", "Запуск бота"),
        BotCommand("login", "Авторизация(для админов)"),
        BotCommand("exit", "Выход")
    ]
    await bot.set_my_commands(commands)

async def on_startup(dp):
    await db.create_connection()
    await set_commands(bot)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
    
    