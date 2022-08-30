from loader import DEBUG


# * Функция вывода ошибок в обработчиках исключений
async def debugger(error: Exception) -> Exception:
	if DEBUG:
		return error
