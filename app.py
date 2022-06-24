#!/usr/bin/python3.8
import os
import middlewares


async def startup_func(dp):
    from aiogram.types import BotCommand
    commands = [
        BotCommand("start", "Запуск бота"),
        BotCommand("help", "Информация о боте"),
        BotCommand("exit", "Выход из режима ввода данных")
    ]
    middlewares.setup(dp)
    await dp.bot.set_my_commands(commands)


def setup_django():
    import django
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_admin.django_admin.settings'
    os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
    django.setup()


if __name__ == '__main__':
    setup_django()

    from aiogram import executor
    import filters
    import handlers
    from loader import dp, bot
    executor.start_polling(dp, on_startup=startup_func)
