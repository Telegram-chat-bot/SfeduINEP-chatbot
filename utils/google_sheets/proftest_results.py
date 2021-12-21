import gspread
from oauth2client.service_account import ServiceAccountCredentials
from asgiref.sync import sync_to_async


@sync_to_async
def get_results(user_id, directions):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("utils/google_sheets/creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("Тест на профориентацию (Ответы)").sheet1

    # Получаем id пользователя
    get_rows_id = sheet.findall(user_id)

    # Получение номера строки, где лежит id
    rows = [row.row for row in get_rows_id]

    # Получаем время завешршения теста
    date = sheet.row_values(rows[-1])[0]

    # Добавляем баллы в массив
    test_data = sheet.row_values(rows[-1])[3:]

    scores = {}  # словарь с вычисленным результатом
    first, last = 0, 3
    for k, v in directions.items():
        scores.setdefault(f"{k} - {v}", 0)  # добавление кода направлений с значением 0 по умолчанию
        for point in test_data[first:last]:
            scores[f"{k} - {v}"] += int(point)  # на каждое направление суммируются баллы из каждых трех вопросов
        first += 3
        last += 3

    max_point = max(scores.values())
    sorted_scores = [(k, scores[k]) for k in
                     sorted(scores, key=scores.get, reverse=True)]  # Сортировка направлений по баллам

    points = [f"{dir_point[0]}: <i>{dir_point[1]}</i>" for dir_point in sorted_scores]  # Представление результатов

    # Итоговые наиболее подходящие направления для абитуриента
    result = [f"<b>{direction}</b>" for direction, point in scores.items() if point == max_point]

    return (
            f"<b>Результаты теста, выполненного <i>{date}</i></b>\n\n"
            + "<u>Баллы по направлениям</u>\n"
            + "\n".join(points)
            + '\n\nПодведя итоги, могу сказать, что более всего для вас подходит(-ят) направление(-я)\n'
            + "\n".join(result)
    )
