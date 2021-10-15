from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Инлайн кнопки выбора ролей--------
abitr_role = InlineKeyboardButton(text="Абитуриент", callback_data="abtr")
student_role = InlineKeyboardButton(text="Студент", callback_data="std")
teacher_role = InlineKeyboardButton(text="Преподаватель", callback_data="tch")

roles = InlineKeyboardMarkup().add(abitr_role, student_role, teacher_role)

#Инлайн кнопки выбора языка---------
lang1 = InlineKeyboardButton(text="Русский", callback_data="ru")
lang2 = InlineKeyboardButton(text="English", callback_data="en")
lang3 = InlineKeyboardButton(text="Espanol", callback_data="es")

lang_key = InlineKeyboardMarkup().add(lang1, lang2, lang3)

#Инлайн кнопки выбора уровня образования----------
bak_level = InlineKeyboardButton(text="Бакалавриат/Специалитет", callback_data="bak")
mag_level = InlineKeyboardButton(text="Магистратура", callback_data="mag")

choose_level = InlineKeyboardMarkup().add(bak_level,mag_level)

#ссылка правила приема---------------   НУЖНО ДОБАВИТЬ РАЗДЕЛЫ НА БАК И МАГ
rules_of_reception = InlineKeyboardButton(text="Ссылка", url = "https://sfedu.ru/www/stat_pages22.show?p=ABT/N8202")#поменять ссылки
rules = InlineKeyboardMarkup().add(rules_of_reception)

#ссылка направления подготовки(бак,маг)---------------------
training_directions_bak = InlineKeyboardButton(text = "Ссылка",url ="https://sfedu.ru/www/stat_pages22.show?p=ABT/N8206/P")#поменять ссылки
train_bak = InlineKeyboardMarkup().add(training_directions_bak)

training_directions_mag = InlineKeyboardButton(text = "Ссылка",url ="https://sfedu.ru/www/stat_pages22.show?p=ABT/N8207/P")#поменять ссылки
train_mag = InlineKeyboardMarkup().add(training_directions_mag)

#ссылка вступительные исыпатния(надо изменить)-------------------
challeng_mag = InlineKeyboardButton(text = "ссылка",url = "https://sfedu.ru/www/stat_pages22.show?p=ABT/N8211/P")#поменять ссылки
challeng_bak = InlineKeyboardButton(text = "ссылка",url = "https://sfedu.ru/www/stat_pages22.show?p=ABT/N8211/P")#поменять ссылки
challengs_mag = InlineKeyboardMarkup().add(challeng_mag)
challengs_bak = InlineKeyboardMarkup().add(challeng_bak)


