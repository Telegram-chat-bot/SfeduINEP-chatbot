# Generated by Django 3.2.9 on 2021-12-24 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 24, 16, 28, 58, 528091), verbose_name='Дата отправки отзыва'),
        ),
    ]