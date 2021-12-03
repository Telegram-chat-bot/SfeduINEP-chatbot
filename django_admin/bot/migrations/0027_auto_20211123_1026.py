# Generated by Django 3.2.9 on 2021-11-23 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0026_chatid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatid',
            name='chat_id',
            field=models.BigIntegerField(unique=True, verbose_name='ID чата'),
        ),
        migrations.AlterField(
            model_name='num_places',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.directions', unique=True, verbose_name='Направление подготовки'),
        ),
        migrations.AlterField(
            model_name='passing_scores',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.directions', unique=True, verbose_name='Направление подготовки'),
        ),
        migrations.AlterField(
            model_name='proftest',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.directions', unique=True, verbose_name='Направления'),
        ),
    ]