# Generated by Django 3.2.9 on 2021-11-23 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0027_auto_20211123_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatid',
            name='chat_direction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bot.directions', verbose_name='Чат для направления подготовки:'),
        ),
    ]
