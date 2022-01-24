from asgiref.sync import sync_to_async
from django.db.models import Q
from Django_apps.bot.models import *
from Django_apps.service.models import  *
from Django_apps.feedback.models import *


# -----------------------------------------
# Получение данных для раздела Поступление
# Получение данных о правилах приема
@sync_to_async
def get_admission_rules():
    return Admission.objects.values_list("admission_rules")[0]


# Получение данных Подать документы
@sync_to_async
def get_admission_submit_doc():
    return Admission.objects.values_list("submit_doc")[0]


# Получение данных для раздела Проходные баллы
@sync_to_async
def get_admission_passing_scores(id: str):
    return Passing_scores.objects.get(direction_id=id).inf


# Получение данных для раздела Количество мест
@sync_to_async
def get_admission_num_places(id: str):
    return Num_places.objects.get(direction_id=id).inf


# Получение данных о Индивидуальных достижениях
@sync_to_async
def get_admission_achievements():
    return Admission.objects.values_list("achievements")[0]


# Получение данных о Особых льготах
@sync_to_async
def get_admission_spec_rights():
    return Admission.objects.values_list("special_rights")[0]


# Получение данных о статистике приема
@sync_to_async
def get_admission_stat():
    return Admission.objects.values_list("admission_stat")[0]


# Получение данных о Порядке поступления
@sync_to_async
def get_admission_enrollment_proc():
    return Admission.objects.values_list("enrollment_proc")[0]


# --------------------------------------------


# Получение данных для раздела Об институте
# Получение данных о разделе Знакомства
@sync_to_async
def get_about_acquaintance():
    return About.objects.values_list("acquaintance")[0]


# Получение данных об Экскурсиях
@sync_to_async
def get_about_excursion():
    return About.objects.values_list("excursion")[0]


# Получение данных о науке
@sync_to_async
def get_about_science():
    return About.objects.values_list("science")[0]


# Получение данных о Событиях
@sync_to_async
def get_about_events():
    return About.objects.values_list("events")[0]


# Получение данных о Партнерах и трудоустройстве
@sync_to_async
def get_about_partners_work():
    return About.objects.values_list("partners_work")[0]


# Получение данных о Студсовете
@sync_to_async
def get_about_council():
    return About.objects.values_list("stud_council")[0]


# Получение данных о фото
@sync_to_async
def get_about_photo():
    return About.objects.values_list("photo")[0]


# Получение данных о контактах
@sync_to_async
def get_about_contacts():
    return About.objects.values_list("contacts")[0]


# -------------------------------------------
# Получение данных о направлениях подготовки
@sync_to_async
def get_directions():
    return Directions.objects.values()


# Получение кода направлений
# @sync_to_async
# def get_dir_code():
#     return [el.direction for el in Directions.objects.all()]


# Получение направлений для ПРОФ.ТЕСТА
@sync_to_async
def get_bak_directions():
    return {
        k["direction"]: k["name_of_dir"] for k in
        Directions.objects.filter(Q(level="bak") | Q(level="spec")).values("direction", "name_of_dir")
    }


# Получение данных для раздела FAQ
@sync_to_async
def get_faq():
    return Questions.objects.all().values_list("faq")[0][0]


# --------------------------------------------
# Получение приветственного сообщения
@sync_to_async
def get_welcome_msg():
    return Welcome_message.objects.all().values_list("message")[0][0]


# Получение ID чата для направления подготовки
@sync_to_async
def get_chat_id_group_directions(code):
    origin_data = Directions.objects.get(direction=code).id
    return ChatIDDirections.objects.get(chat_direction_id=origin_data).chat_id


# Получение ID чата для вопросов по поступлению
@sync_to_async
def get_chat_id_admission():
    return ChatIDAdmission.objects.all().values_list('chat_id')[0][0]


# ЗАПИСЬ ДАННЫХ В БАЗУ ДАННЫХ
# Запись id чата по поступлению
@sync_to_async
def save_chat_id_group_admission(group_id: str):
    return ChatIDAdmission(chat_id=group_id).save()


# Запись id чата по направлениям
@sync_to_async
def save_chat_id_group_direction(group_id: str, direction: str):
    return ChatIDDirections(chat_id=group_id, chat_direction=direction).save()


# Проверка на существование id чата в бд
@sync_to_async
def isChatExist(chat_id: str):
    return ChatIDDirections.objects.filter(chat_id=chat_id).exists() or ChatIDAdmission.objects.filter(
        chat_id=chat_id).exists()


# Удаление id чата группы
@sync_to_async
def del_chat_id(chat_id: str):
    try:
        return ChatIDAdmission.objects.get(chat_id=chat_id).delete()
    except:
        ChatIDDirections.objects.get(chat_id=chat_id).delete()


# Сохранение отзыва
@sync_to_async
def send_feedback(username: str, review: str):
    Feedback(username=username, review=review).save()


# Добавление id пользователя в бд после нажатия команды start
@sync_to_async
def add_user(name: str, uid: int):
    try:
        return Users.objects.update_or_create(
            username=name,
            user_id=uid
        )
    except:
        return None


# Получение id всех пользователей, которые когда либо общались с ботом
@sync_to_async
def get_users():
    return Users.objects.all().values_list("user_id")
