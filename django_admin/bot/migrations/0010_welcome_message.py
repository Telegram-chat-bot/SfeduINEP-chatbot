# Generated by Django 3.2.9 on 2021-11-15 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_alter_directions_inf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Welcome_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Текст приветствия')),
            ],
            options={
                'verbose_name': 'приветствие',
                'verbose_name_plural': 'Приветствие бота',
            },
        ),
    ]
