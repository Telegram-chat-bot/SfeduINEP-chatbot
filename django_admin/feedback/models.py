from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    class Meta:
        app_label = "feedback"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    review = models.TextField(
        verbose_name="Отзыв"
    )
    username = models.CharField(
        verbose_name="Никнейм",
        max_length=50
    )
    created_at = models.DateTimeField(
        verbose_name="Дата отправки отзыва",
        default=timezone.now
    )

    def __str__(self):
        return self.username
