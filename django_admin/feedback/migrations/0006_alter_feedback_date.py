# Generated by Django 3.2.9 on 2021-12-24 13:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_alter_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 24, 13, 36, 19, 684688, tzinfo=utc), verbose_name='Дата отправки отзыва'),
        ),
    ]
