# Generated by Django 3.2.9 on 2021-12-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_alter_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(verbose_name='Дата отправки отзыва'),
        ),
    ]
