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
bakalav_level = InlineKeyboardButton(text="Бакалавриат\Специалитет", callback_data="baka")
magistrat_level = InlineKeyboardButton(text="Магистратура", callback_data="maga")

choose_level = InlineKeyboardMarkup().add(bakalav_level,magistrat_level)

#
