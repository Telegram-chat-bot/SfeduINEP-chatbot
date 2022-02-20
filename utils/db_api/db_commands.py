from asgiref.sync import sync_to_async
from django.db.models import Q
from django_admin.bot.models import *
from django_admin.service.models import  *
from django_admin.feedback.models import *


# -----------------------------------------

class AdmissionData:
    data = Admission.objects.all()[0]

    @classmethod
    @sync_to_async
    def admission_rules(cls):
        return cls.data.admission_rules

    @classmethod
    @sync_to_async
    def submit_doc(cls):
        return cls.data.submit_doc

    @classmethod
    @sync_to_async
    def achievements(cls):
        return cls.data.achievements

    @classmethod
    @sync_to_async
    def special_rights(cls):
        return cls.data.special_rights

    @classmethod
    @sync_to_async
    def admiss_stat(cls):
        return cls.data.admission_stat

    @classmethod
    @sync_to_async
    def enrollment_procedure(cls):
        return cls.data.enrollment_proc


class AboutData:
    data = About.objects.all()[0]

    @classmethod
    @sync_to_async
    def acquaintance(cls):
        return cls.data.acquaintance

    @classmethod
    @sync_to_async
    def excursion(cls):
        return cls.data.excursion

    @classmethod
    @sync_to_async
    def science(cls):
        return cls.data.science

    @classmethod
    @sync_to_async
    def contacts(cls):
        return cls.data.contacts

    @classmethod
    @sync_to_async
    def events(cls):
        return cls.data.events

    @classmethod
    @sync_to_async
    def partners_work(cls):
        return cls.data.partners_work

    @classmethod
    @sync_to_async
    def council(cls):
        return cls.data.stud_council

    @classmethod
    @sync_to_async
    def photo(cls):
        return cls.data.photo


# Получение данных для раздела Проходные баллы
@sync_to_async
def get_admission_passing_scores(id: str):
    return Passing_scores.objects.get(direction_id=id).inf


# Получение данных для раздела Количество мест
@sync_to_async
def get_admission_num_places(id: str):
    return Num_places.objects.get(direction_id=id).inf

# --------------------------------------------


# Получение данных о направлениях подготовки
@sync_to_async
def get_directions():
    return Directions.objects.values()


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
    return Questions.objects.all().values_list("faq")[0]


# --------------------------------------------
# Получение приветственного сообщения
@sync_to_async
def get_welcome_msg():
    return Welcome_message.objects.all().values_list("message")[0]


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
        return ChatIDDirections.objects.get(chat_id=chat_id).delete()


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


@sync_to_async
def get_help_text(chat_type:str):
    try:
        return Help_content.objects.filter(target_user=chat_type).values_list("content")[0][0]
    except:
        return "В этот раздел ещё не добавили информацию"


@sync_to_async
def openday_inf():
    return OpenDay.objects.values_list("inf")[0]