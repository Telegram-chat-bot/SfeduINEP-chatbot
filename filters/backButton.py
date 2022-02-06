from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class CommandBack(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.text == "Назад"
