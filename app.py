#!/usr/bin/python3.8
import os
import middlewares
from utils.scheduler.delete_scheduler import delete_old_feedback
from utils.bot_commands import commands
from utils.db_api.backup_module import DatabaseDump
import utils.logger
import asyncio
import aioschedule as schedule


async def startup(dp) -> None:
    await setup_django()
    await commands.setup_commands(dp)
    middlewares.setup(dp)
    asyncio.create_task(scheduler())


async def scheduler() -> None:
    schedule.every().day.at("4:00").do(delete_old_feedback)
    # schedule.every(2).seconds.do(DatabaseDump.make_dump)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)


async def setup_django() -> None:
    import django
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_admin.django_admin.settings'
    os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
    django.setup()


if __name__ == '__main__':
    main_loop = asyncio.get_event_loop()
    main_loop.run_until_complete(setup_django())

    from aiogram import executor
    import filters
    import handlers
    from loader import dp, bot
    executor.start_polling(dp, on_startup=startup)
