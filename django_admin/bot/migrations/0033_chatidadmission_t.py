# Generated by Django 3.2.9 on 2021-12-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0032_auto_20211206_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatidadmission',
            name='t',
            field=models.BooleanField(default=False, verbose_name='Test'),
        ),
    ]
