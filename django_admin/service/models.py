from django.db import models
from django.db.models.deletion import CASCADE
from django_admin.bot.models import Directions


class ChatIDDirections(models.Model):
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


class ChatIDAdmission(models.Model):
    class Meta:
        verbose_name = "ID чата"
        verbose_name_plural = "ID чата по вопросам поступлению"
        app_label = "service"

    chat_id = models.BigIntegerField(
        verbose_name="ID чата",
        unique=True
    )

    def __str__(self) -> str:
        return "Чат для вопросов по поступлению"


class Users(models.Model):
    class Meta:
        verbose_name = "ID пользователя"
        verbose_name_plural = "ID пользователей"
        app_label = "service"

    username = models.CharField(
        verbose_name="Никнейм пользователя",
        max_length=50
    )

    user_id = models.BigIntegerField(
        verbose_name="user id",
        unique=True
    )

    def __str__(self):
        return f"{self.username}"
