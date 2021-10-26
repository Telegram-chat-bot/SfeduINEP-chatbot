from loader import bot, dp, item
from aiogram.types import CallbackQuery, message, InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline import buttons as btn

def init_url(link):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Перейти к источнику",
                    url=link
                )
            ],
            [
                btn.back_btn
            ]
        ]
    )

@dp.callback_query_handler(lambda call: call.data)
async def direct_of_prepare_handler(call: CallbackQuery):
    for direction, value in directions[str(item[0])].items():
        if call.data == direction:
            if item[0] == 1:
                await call.message.edit_text("Всю информацию по данному направлению вы можете найти, перейдя по ссылке", reply_markup=init_url(link=value))
            elif item[0] in [2, 3]:
                await call.message.edit_text(f"{direction}\n{value}", reply_markup=InlineKeyboardMarkup().add(btn.back_btn))


directions = {
    "1":{
        #Бакалавриат
        "11.03.03": "https://inep.sfedu.ru/chairs/kes/",
        "11.03.04": "https://inep.sfedu.ru/chairs/rte/",
        "12.03.01": "https://inep.sfedu.ru/chairs/egaimt/egaimt-abiturient/#120304",
        "12.03.04": "https://inep.sfedu.ru/chairs/egaimt/egaimt-abiturient/#120304",
        "20.03.01": "https://inep.sfedu.ru/chairs/tbh/tbh-abiturient/",
        "28.03.02": "https://sfedu.ru/www/stat_pages22.show?p=EDU/annot/D&params=%28p_specia_id=%3E3908%29",
        
        #Специалитет
        "26.05.04": "https://inep.sfedu.ru/wp-content/uploads/2014/12/05/buklet_26-05-04-111.pdf",

        #Магистратура
        "09.04.03": "https://inep.sfedu.ru/wp-content/uploads/2020/12/19/%D0%91%D1%83%D0%BA%D0%BB%D0%B5%D1%82090403_18_12_2020_%D0%98%D0%9D%D0%AD%D0%9F.pdf",
        "11.04.00": "https://vk.com/video-52679049_456239057",
        "12.04.00": "https://sfedu.ru/www/stat_pages22.show?p=EDU/annot/D&params=%28p_specia_id=%3E3892%29",
        "20.04.01": "https://inep.sfedu.ru/wp-content/uploads/2014/12/08/%D0%A2%D0%B5%D1%85%D0%BD%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%BD%D0%B0%D1%8F-%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C.pdf",
        "28.04.01": "http://sfedu.ru/00_main_2010/abitur/abit_2018/magist_ekz/28_04_01_program_mag_2018.pdf",
        "28.04.02": "https://vk.com/video-52679049_456239061"
    },

    "2":{
        #Бакалавриат
        "11.03.03": """
Русский язык: 50
Математика: 50
Физика/Информатика и ИКТ: 50
                    """,

        "11.03.04": """
Русский язык: 50
Математика: 50
Физика/Информатика и ИКТ: 50
                    """,

        "12.03.01": """
Русский язык: 50
Математика: 50
Физика/Информатика и ИКТ: 50
                    """,

        "12.03.04": """
Русский язык: 50
Математика: 50
Физика/Информатика и ИКТ/Биология: 50
                    """,

        "20.03.01": """
Русский язык: 50
Математика: 50
Физика/Информатика и ИКТ/Химия: 50
                    """,

        "28.03.02": """
Русский язык: 50
Математика: 50
Физика/Информатика и ИКТ/Химия: 50
                    """,
        
        #Специалитет
        "26.05.04": """
Русский язык: 50
Математика: 50
Физика/Информатика и ИКТ: 50
                    """,

        #Магистратура
        "09.04.03": """Экзамен по направлению подготовки:\nhttps://inep.sfedu.ru/wp-content/uploads/2019/02/18/Prog_prikl_inf.pdf
                    """,
                    
        "11.04.00": """
        Экзамен по направлению подготовки:\nhttp://sfedu.ru/00_main_2010/abitur/abit_2018/magist_ekz/11_04_03_program_mag_2018.pdf
                    """,

        "12.04.00": """
        Экзамен по направлению подготовки:\nhttp://sfedu.ru/00_main_2010/abitur/abit_2018/magist_ekz/12_04_04_program_mag_2018.pdf
                    """,
       
        "20.04.01": """
        Экзамен по направлению подготовки:\nhttp://sfedu.ru/00_main_2010/abitur/abit_2018/magist_ekz/20_04_01_program_mag_2018.pdf
                    """,

        "28.04.01": """
        Экзамен по направлению подготовки:\nhttp://sfedu.ru/00_main_2010/abitur/abit_2018/magist_ekz/28_04_01_program_mag_2018.pdf
                    """,

        "28.04.02": """
        Экзамен по направлению подготовки:\nhttp://sfedu.ru/00_main_2010/abitur/abit_2018/magist_ekz/28_04_01_program_mag_2018.pdf 
        """
    },

    "3":{
        #Бакалавриат
        "11.03.03": """
25 - гос. бюджет
0 - полное возмещение затрат
        """,
        
        "11.03.04": """
25 - гос. бюджет
0 - полное возмещение затрат
        """,
        
        "12.03.01": """
22 - гос. бюджет
3 - полное возмещение затрат
        """,

        "12.03.04": """
24 - гос. бюджет
5 - полное возмещение затрат
        """,

        "20.03.01": """
22 - гос. бюджет
3 - полное возмещение затрат
        """,

        "28.03.02": """
25 - гос. бюджет
1 - полное возмещение затрат
        """,
        
        #Специалитет
        "26.05.04": """
25 - гос. бюджет
0 - полное возмещение затрат
        """,

        #Магистратура
        "09.04.03": """
20 - гос. бюджет
5 - полное возмещение затрат
        """,

        "11.04.00": """
20 - гос. бюджет
5 - полное возмещение затрат
        """,

        "12.04.00":  """
15 - гос. бюджет
5 - полное возмещение затрат
        """,

        "20.04.01": """
25 - гос. бюджет
0 - полное возмещение затрат
        """,

        "28.04.01": """
12 - гос. бюджет
3 - полное возмещение затрат
        """,
        
        "28.04.02": """
0 - гос. бюджет
15 - полное возмещение затрат
        """
    }
}