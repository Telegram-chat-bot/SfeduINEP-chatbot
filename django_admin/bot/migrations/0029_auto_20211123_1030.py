# Generated by Django 3.2.9 on 2021-11-23 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0028_alter_chatid_chat_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='num_places',
            name='direction',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.directions', verbose_name='Направление подготовки'),
        ),
        migrations.AlterField(
            model_name='passing_scores',
            name='direction',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.directions', verbose_name='Направление подготовки'),
        ),
    ]
