from django.db import models


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
    date = models.DateField(
        verbose_name="Дата отправки отзыва",
        auto_now_add=True
    )

    def __str__(self):
        return self.username
