# Generated by Django 3.2.9 on 2021-11-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0013_auto_20211120_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proftest',
            old_name='question',
            new_name='question1',
        ),
        migrations.AddField(
            model_name='proftest',
            name='question2',
            field=models.TextField(null=True),
        ),
    ]