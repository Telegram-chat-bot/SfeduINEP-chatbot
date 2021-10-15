from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_btn = InlineKeyboardButton(text="Назад", callback_data="back_to")
#Инлайн кнопки выбора языка---------
lang1 = InlineKeyboardButton(text="Русский", callback_data="ru")
lang2 = InlineKeyboardButton(text="English", callback_data="en")
lang3 = InlineKeyboardButton(text="Espanol", callback_data="es")

lang_key = InlineKeyboardMarkup().add(lang1, lang2, lang3)

# Инлайн кнопки выбора ролей--------
abitr_role = InlineKeyboardButton(text="Абитуриент", callback_data="abtr")
student_role = InlineKeyboardButton(text="Студент", callback_data="std")
teacher_role = InlineKeyboardButton(text="Преподаватель", callback_data="tch")

roles = InlineKeyboardMarkup().add(abitr_role, student_role, teacher_role)

#Инлайн кнопки выбора уровня образования----------
bak_level = InlineKeyboardButton(text="Бакалавриат", callback_data="bak")
spec_level = InlineKeyboardButton(text="Специалитет", callback_data="spec")
mag_level = InlineKeyboardButton(text="Магистратура", callback_data="mag")

choose_level = InlineKeyboardMarkup().add(bak_level, spec_level, mag_level)

#Специальности бакалавра
bak1 = InlineKeyboardButton(text="11.03.03 «Конструирование и технология электронных средств»", callback_data="11.03.03")
bak2 = InlineKeyboardButton(text="11.03.04 «Электроника и наноэлектроника»", callback_data="11.03.04")
bak3 = InlineKeyboardButton(text="12.03.01 «Приборостроение»", callback_data="12.03.01")
bak4 = InlineKeyboardButton(text="12.03.04 «Биотехнические системы и технологии»", callback_data="12.03.04")
bak5 = InlineKeyboardButton(text="17.03.01 “Корабельное вооружение”", callback_data="17.03.01")
bak6 = InlineKeyboardButton(text="20.03.01 «Техносферная безопасность»", callback_data="20.03.01")
bak7 = InlineKeyboardButton(text="21.03.02 «Землеустройство и кадастры»", callback_data="21.03.02")
bak8 = InlineKeyboardButton(text=" 27.03.01 «Стандартизация и метрология»", callback_data="27.03.01")
bak9 = InlineKeyboardButton(text="28.03.01 «Нанотехнологии и микросистемная техника»", callback_data="28.03.01")
bak10 = InlineKeyboardButton(text="28.03.02 «Наноинженерия»", callback_data="28.03.02")

bak_prepare_direct = InlineKeyboardMarkup(row_width=1).add(bak1, bak2, bak3, bak4, bak5, bak6, bak7, bak8, bak9, bak10, back_btn)

#Специалитет
spec1 = InlineKeyboardButton(text="26.05.04 «Применение и эксплуатация технических систем надводных кораблей и подводных лодок»", callback_data="26.05.04")
spec_prepare_direct = InlineKeyboardMarkup(row_width=1).add(spec1, back_btn)

#Магистратура
mag1 = InlineKeyboardButton(text="11.04.03 «Конструирование и технология электронных средств»", callback_data="11.04.03")
mag2 = InlineKeyboardButton(text="11.04.04 «Электроника и наноэлектроника»", callback_data="11.04.04")
mag3 = InlineKeyboardButton(text="12.04.01 «Приборостроение»", callback_data="12.04.01")
mag4 = InlineKeyboardButton(text="12.04.04 «Биотехнические системы и технологии»", callback_data="12.04.04")
mag5 = InlineKeyboardButton(text="20.04.01 «Техносферная безопасность»", callback_data="20.04.01")
mag6 = InlineKeyboardButton(text="28.04.01 «Нанотехнологии и микросистемная техника»", callback_data="28.04.01")

mag_prepare_direct = InlineKeyboardMarkup(row_width=1).add(mag1, mag2, mag3, mag4, mag5, mag6, back_btn)

#ссылка вступительные исыпатния(надо изменить)-------------------
challeng_mag = InlineKeyboardButton(text = "ссылка",url = "https://sfedu.ru/www/stat_pages22.show?p=ABT/N8211/P")#поменять ссылки
challeng_bak = InlineKeyboardButton(text = "ссылка",url = "https://sfedu.ru/www/stat_pages22.show?p=ABT/N8211/P")#поменять ссылки
challengs_mag = InlineKeyboardMarkup().add(challeng_mag)
challengs_bak = InlineKeyboardMarkup().add(challeng_bak)