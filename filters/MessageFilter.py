from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class IsNotButton(BoundFilter):
	def __init__(self, buttons: list):
		self.buttons = buttons

	async def check(self, message: types.Message) -> bool:
		if message.text.startswith("/"):
			return False
		if message.text not in self.buttons:
			return True
		await message.answer("Сначала напишите вопрос или отмените ввод командой /exit")
