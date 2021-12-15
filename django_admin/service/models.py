from django.db import models
from django.db.models.deletion import CASCADE
from django_admin.bot.models import Directions


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = models.Manager()


# Create your models here.
class ChatIDDirections(BaseModel):
    class Meta:
        verbose_name = "ID чата"
        verbose_name_plural = "ID чатов для вопросов по направлению подготовки"
        app_label = "service"

    chat_direction = models.OneToOneField(
        Directions,
        verbose_name="Чат для направления подготовки:",
        on_delete=CASCADE,
    )
    chat_id = models.BigIntegerField(
        verbose_name="ID чата",
        unique=True
    )

    def __str__(self) -> str:
        return f"{self.chat_direction}"


class ChatIDAdmission(BaseModel):
    class Meta:
        verbose_name = "ID чата"
        verbose_name_plural = "ID чата по поступлению"
        app_label = "service"

    chat_id = models.BigIntegerField(
        verbose_name="ID чата",
        unique=True
    )

    def __str__(self) -> str:
        return "ChatID"
