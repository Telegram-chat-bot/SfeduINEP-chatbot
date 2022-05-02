from asgiref.sync import sync_to_async
from django.db.models import Q, QuerySet
from django_admin.bot.models import *
from django_admin.service.models import *
from django_admin.feedback.models import *
from django.db import models


# -----------------------------------------
class Database:
    def __init__(self, model):
        self.model: models.Model = model
        self.fields = self.model.objects

    async def get_field_by_name(self, field) -> str:
        return getattr(self.fields.get(), field, "Ошибка 404. Поле не существует")

    async def get_collection_data(self, *args: str,
                                  is_dict: bool = False,
                                  get_all: bool = False,
                                  ) -> QuerySet:
        if get_all:
            self.fields = self.model.objects.all()

        if is_dict:
            return self.fields.values(*args)
        else:
            return self.fields.values_list(*args)

    # async def test(self, **data):
    #     return self.fields.get(**data)


# --------------------------------------------
# Проверка на существование id чата в бд
@sync_to_async
def isChatExist(chat_id: str):
    return ChatIDDirections.objects.filter(chat_id=chat_id).exists() or ChatIDAdmission.objects.filter(
        chat_id=chat_id).exists()


# Получение направлений для ПРОФ.ТЕСТА
@sync_to_async
def get_bak_directions():
    return {
        k["direction"]: k["name_of_dir"] for k in
        Directions.objects.filter(Q(level="bak") | Q(level="spec")).values("direction", "name_of_dir")
    }

# --------------------------------------------


# Получение ID чата для направления подготовки
@sync_to_async
def get_chat_id_group_directions(code):
    origin_data = Directions.objects.get(direction=code).id
    return ChatIDDirections.objects.get(chat_direction_id=origin_data).chat_id


# ЗАПИСЬ ДАННЫХ В БАЗУ ДАННЫХ
# Запись id чата по поступлению
@sync_to_async
def save_chat_id_group_admission(group_id: str):
    return ChatIDAdmission(chat_id=group_id).save()


# Запись id чата по направлениям
@sync_to_async
def save_chat_id_group_direction(group_id: str, direction: str):
    return ChatIDDirections(chat_id=group_id, chat_direction=direction).save()


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


@sync_to_async
def get_help_text(chat_type: str):
    try:
        return Help_content.objects.filter(target_user=chat_type).values_list("content")[0][0]
    except:
        return "В этот раздел ещё не добавили информацию"


@sync_to_async
def openday_inf():
    return OpenDay.objects.values_list("inf")[0]
