# Generated by Django 3.2.9 on 2021-11-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0021_alter_proftest_direction'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatID',
            fields=[
                ('chat_name', models.CharField(max_length=100, verbose_name='Название чата')),
                ('chat_id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID чата')),
            ],
            options={
                'verbose_name': 'ID чата',
                'verbose_name_plural': 'ID чатов для вопросов',
            },
        ),
    ]
