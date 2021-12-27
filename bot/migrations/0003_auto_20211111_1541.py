# Generated by Django 3.2.9 on 2021-11-11 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20211111_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='num_places',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.directions', verbose_name='Направление подготовки'),
        ),
        migrations.AlterField(
            model_name='passing_scores',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.directions', verbose_name='Направление подготовки'),
        ),
    ]