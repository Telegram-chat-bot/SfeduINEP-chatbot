# Generated by Django 3.2.9 on 2021-11-22 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0025_delete_chatid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField(verbose_name='ID чата')),
                ('chat_direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.directions', verbose_name='Чат для направления подготовки:')),
            ],
            options={
                'verbose_name': 'ID чата',
                'verbose_name_plural': 'ID чатов для вопросов',
            },
        ),
    ]
