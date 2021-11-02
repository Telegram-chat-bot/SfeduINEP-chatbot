from aiogram.bot.bot import Bot
from aiogram.types import BotCommand 
from loader import bot, storage, dp, db
from aiogram import executor

import handlers

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
    await db.create_data_tables()
    await set_commands(bot)

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
    