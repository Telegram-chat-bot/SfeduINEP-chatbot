import logging
import os.path

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from asgiref.sync import sync_to_async
from app import HOME_DIRECTORY


@sync_to_async
def get_results(user_id, directions):
    scope = [
        "https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"
    ]
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            os.path.join(HOME_DIRECTORY, "utils/google_sheets/creds.json"), scope
        )

        client = gspread.authorize(creds)

        sheet = client.open("Тест на профориентацию (Ответы)").sheet1

        # * Получаем id пользователя
        get_rows_id = sheet.findall(user_id)

        if len(get_rows_id):
            # * Получение номера строки, где лежит id
            rows = [row.row for row in get_rows_id]

            # * Получаем время завешршения теста
            date = sheet.row_values(rows[-1])[0]

            # * Добавляем баллы в массив
            test_data = sheet.row_values(rows[-1])[3:]

            # * словарь с вычисленным результатом
            scores: dict = {}
            first, last = 0, 3
            for k, v in directions.items():
                scores.setdefault(f"{k} - {v}", 0)  # * добавление кода направлений с значением 0 по умолчанию
                for point in test_data[first:last]:
                    scores[f"{k} - {v}"] += int(
                        point)  # * на каждое направление суммируются баллы из каждых трех вопросов
                first += 3
                last += 3

            max_point: int = max(scores.values())
            # * Сортировка направлений по баллам
            sorted_scores: list = [(k, scores[k]) for k in
                                   sorted(scores, key=scores.get, reverse=True)]

            # Представление результатов
            points: list = [
                # Название направления балл
                f"{dir_point[0]}: <b><i>{dir_point[1]}</i></b> {'балл' if (dir_point[1] % 10 == 1 and dir_point[1] != 11) else 'балла' if (dir_point[1] % 10 in [2, 3, 4] and dir_point[1] not in [12, 13, 14]) else 'баллов'}"
                for dir_point in sorted_scores
            ]

            # Итоговые наиболее подходящие направления для абитуриента
            result: list = [f"<b>{direction}</b>" for direction, point in scores.items() if
                            (point == max_point and point != 0)]
            suitable_dir: str = f"{'на направлении' if len(result) == 1 else 'на направлениях'}"

            return (
                    f"<b>Результаты теста, выполненного <i>{date}</i></b>\n\n"
                    + "<u>Баллы по направлениям</u>\n"
                    + "\n".join(points)
                    + f"\n\n{f'Подведя итоги, могу сказать, что вы хотите учиться {suitable_dir}' if len(result) else 'Вам не подходит ни одно направление'}\n"
                    + "\n".join(result)
            )
        else:
            return "Вы еще не прошли профориентационный тест"

    except FileNotFoundError:
        logging.error("File creds.json not found")

