from asgiref.sync import sync_to_async
from django.db.models import Q

from django_admin.service.models import *
from django.db import models


class Database:
    def __init__(self, model):
        self.model: models.Model = model
        self.objects = self.model.objects

    async def get_field_by_name(self, field) -> str:
        return getattr(self.objects.get(), field, "Ошибка 404. Поле не существует")

    async def get_field_by_key(self, **kwargs):
        return self.objects.get(**kwargs)

    async def get_collection_data(self, *args,
                                  is_dict: bool = False,
                                  get_all: bool = False
                                  ):
        if get_all:
            self.objects = self.model.objects.all()

        if is_dict:
            return self.objects.values(*args)

        return self.objects.values_list(*args)


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


# Получение ID чата для направления подготовки
@sync_to_async
def get_chat_id_group_directions(code):
    origin_data = Directions.objects.get(direction=code).id
    return ChatIDDirections.objects.get(chat_direction_id=origin_data).chat_id


# Удаление id чата группы
@sync_to_async
def del_chat_id(chat_id: str):
    try:
        ChatIDAdmission.objects.get(chat_id=chat_id).delete()
    except Exception as error:
        ChatIDDirections.objects.get(chat_id=chat_id).delete()
        return error
