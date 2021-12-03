import gspread
from oauth2client.service_account import ServiceAccountCredentials
from asgiref.sync import sync_to_async

@sync_to_async
def get_results(user_id, directions):
    
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("utils/google_sheets/creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("Тест на профориентацию (Ответы)").sheet1


    get_rows_id = sheet.findall(user_id)
    rows = [row.row for row in get_rows_id]
    date = sheet.row_values(rows[-1])[0]
    test_data = sheet.row_values(rows[-1])[3:]


    scores = {}
    i, j = 0, 3
    for k, v in directions.items():
        scores.setdefault(f"{k} - {v}", 0)
        for point in test_data[i:j]:
            scores[f"{k} - {v}"] += int(point)
        i += 3
        j += 3

    max_point = max(scores.values())
    sorted_scores = [(k, scores[k]) for k in sorted(scores, key=scores.get, reverse=True)]
    
    points = [f"{dir_point[0]}: <i>{dir_point[1]}</i>" for dir_point in sorted_scores]
    result = [f"<b>{direction}</b>" for direction, point in scores.items() if point == max_point]

    return (
        f"<b>Результаты теста, выполненного <i>{date}</i></b>\n\n"
        + "Баллы по направлениям\n"
        + "\n".join(points)
        + '\n\nПодведя итоги, могу сказать, что более всего для вас подходит направление(-я)\n'
        + "\n".join(result)
    )