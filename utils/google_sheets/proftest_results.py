import logging
import os

import gspread_asyncio
from oauth2client.service_account import ServiceAccountCredentials

from django_admin.django_admin.settings import ROOT_DIR


async def right_word(word: str, quantity: int) -> str:
    if (quantity % 10 == 1) and (quantity != 11):
        return word
    elif (1 < quantity % 10 < 5) and not (11 < quantity < 15):
        return f"{word}а"
    else:
        return f"{word}ов"


def init_creds() -> ServiceAccountCredentials:
    scope = ["https://spreadsheets.google.com/feeds",
             'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    return ServiceAccountCredentials.from_json_keyfile_name(
        os.path.join(ROOT_DIR, "utils/google_sheets/creds.json"), scope
    )


async def get_results(user_id: str, directions: dict) -> str:
    try:
        gspread_client_manager = gspread_asyncio.AsyncioGspreadClientManager(init_creds)
        client = await gspread_client_manager.authorize()
        spread_sheet = await client.open("Тест на профориентацию (Ответы)")
        worksheet = await spread_sheet.worksheet("Ответы на форму (1)")

        # client = gspread.authorize(creds)
        # sheet = client.open("Тест на профориентацию (Ответы)").sheet1

        # * Получаем id пользователя
        # get_rows_id: list = sheet.findall(user_id)
        get_rows_id: list = await worksheet.findall(user_id)

        if not get_rows_id:
            return "Вы еще не прошли профориентационный тест"

        # * Получение номера строки, где лежит id
        rows = [row.row for row in get_rows_id]

        # * Получаем время завершения теста
        # date = sheet.row_values(rows[-1])[0]
        date = (await worksheet.row_values(rows[-1]))[0]

        # * Добавляем баллы в массив. Баллы извлекаются, начиная с третьего столбца
        # test_data = sheet.row_values(rows[-1])[3:]
        test_data = (await worksheet.row_values(rows[-1]))[3:]

        # * словарь с вычисленным результатом
        scores: dict = {}

        # * шаги для перехода от одной группе вопросов к другой
        first, last = 0, 3
        for k, v in directions.items():
            scores.setdefault(f"{k} - {v}", 0)  # * добавление кода направлений со значением 0 по умолчанию
            for point in test_data[first:last]:
                # * на каждое направление суммируются баллы из каждых трех вопросов
                scores[f"{k} - {v}"] += int(point)
            first += 3
            last += 3

        max_point: int = max(scores.values())
        # * Сортировка направлений по баллам
        sorted_scores: list = [(k, scores[k]) for k in sorted(scores, key=scores.get, reverse=True)]

        # * Таблица результатов
        result_table: list = [
            # Название направления: балл
            f"{dir_point[0]}: <b><i>{dir_point[1]}</i></b> {await right_word('балл', dir_point[1])}"
            for dir_point in sorted_scores
        ]

        # * Итоговые наиболее подходящие направления для абитуриента
        result_directions: list = [
            f"<b>{direction}</b>" for direction, point in scores.items() if (point == max_point and point)
        ]
        suitable_dir: str = f"{'на направлении' if len(result_directions) == 1 else 'на направлениях'}"

        return (
                f"<b>Результаты теста, выполненного <i>{date}</i></b>\n\n"
                + "<ins>Баллы по направлениям</ins>\n"
                + "\n".join(result_table)
                + f"\n\n{f'Подведя итоги, могу сказать, что вы хотите учиться {suitable_dir}' if result_directions else 'Вам не подходит ни одно направление'}\n"
                + "\n".join(result_directions)
        )
    except FileNotFoundError:
        logging.error("File creds.json not found")
        return "Ошибка! Отсутствует файл с данными для авторизации"
