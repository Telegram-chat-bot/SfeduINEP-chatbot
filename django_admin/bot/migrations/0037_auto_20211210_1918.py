# Generated by Django 3.2.9 on 2021-12-10 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0036_chatidadmission_chatiddirections'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatIDAdmission',
        ),
        migrations.DeleteModel(
            name='ChatIDDirections',
        ),
    ]
