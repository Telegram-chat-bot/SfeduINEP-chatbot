from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from loader import bot
import re


class IsNotButton(BoundFilter):
	def __init__(self, buttons: list):
		self.buttons = buttons

	async def check(self, message: types.Message) -> bool:
		if message.text not in self.buttons and message.text != "/exit":
			return True
		elif message.text == "/exit":
			return False
		await message.answer("Сначала напишите вопрос или отмените ввод командой /exit")


class OtherWords(BoundFilter):
	def __init__(self, service_words: list):
		self.service_words = service_words

	async def check(self, message: types.Message):
		bot_instance = await bot.get_me()
		bot_username = bot_instance.username

		is_chat_command = re.match(r'/\w+@' + bot_username, message.text)
		return message.text not in self.service_words and not is_chat_command

