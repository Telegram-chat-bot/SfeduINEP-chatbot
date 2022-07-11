from loader import DEBUG


# * Функция вывода ошибок в обработчиках исключений
async def debugger(error: str) -> str:
	if DEBUG:
		return error