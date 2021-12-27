# Generated by Django 3.2.9 on 2021-11-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0017_alter_proftest_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proftest',
            name='question1',
        ),
        migrations.RemoveField(
            model_name='proftest',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='proftest',
            name='question3',
        ),
        migrations.AddField(
            model_name='proftest',
            name='question',
            field=models.TextField(null=True, verbose_name='Вопросы'),
        ),
    ]