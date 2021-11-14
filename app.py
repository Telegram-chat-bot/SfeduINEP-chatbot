from aiogram.bot.bot import Bot

async def set_commands(bot: Bot):
    from aiogram.types import BotCommand
    commands = [
        BotCommand("start", "Запуск бота")
    ]
    await bot.set_my_commands(commands)

async def on_startup(dp):
    from loader import bot
    await set_commands(bot)

def setup_django():
    import django
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_admin.django_admin.settings'
    os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
    django.setup()

if __name__ == '__main__':
    setup_django()
    
    from aiogram import executor
    from handlers import dp
    
    executor.start_polling(dp, on_startup=on_startup)