# Generated by Django 3.2.9 on 2021-11-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0013_alter_directions_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directions',
            name='name_of_dir',
            field=models.CharField(max_length=100, verbose_name='Название специальности'),
        ),
        migrations.AlterField(
            model_name='directions',
            name='section',
            field=models.CharField(choices=[('direct_of_prepare', 'Направления подготовки'), ('passing_scores', 'Проходные баллы'), ('num_of_places', 'Количество мест')], default='direct_of_prepare', max_length=20, verbose_name='Раздел бота'),
        ),
    ]
