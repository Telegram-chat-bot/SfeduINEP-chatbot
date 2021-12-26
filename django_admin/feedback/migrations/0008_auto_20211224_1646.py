# Generated by Django 3.2.9 on 2021-12-24 13:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0007_alter_feedback_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='date',
        ),
        migrations.AddField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 24, 13, 46, 45, 393489, tzinfo=utc), verbose_name='Дата отправки отзыва'),
        ),
    ]
