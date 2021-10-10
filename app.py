from loader import bot, storage, dp
from aiogram import executor
import handlers


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=on_shutdown)
    
    
