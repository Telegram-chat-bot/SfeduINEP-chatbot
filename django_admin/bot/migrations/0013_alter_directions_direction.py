# Generated by Django 3.2.9 on 2021-11-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0012_auto_20211109_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directions',
            name='direction',
            field=models.CharField(max_length=10, verbose_name='Код направления'),
        ),
    ]
