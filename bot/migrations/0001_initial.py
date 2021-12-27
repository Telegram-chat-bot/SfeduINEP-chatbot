# Generated by Django 3.2.9 on 2021-11-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acquaintance', models.TextField(blank=True, verbose_name='Знакомство')),
                ('excursion', models.TextField(blank=True, verbose_name='Записаться на экскурсию')),
                ('events', models.TextField(blank=True, verbose_name='Мероприятия')),
                ('science', models.TextField(blank=True, verbose_name='Наука и учёба')),
                ('partners_work', models.TextField(blank=True, verbose_name='Партнёры и трудоустройство')),
                ('stud_council', models.TextField(blank=True, verbose_name='Студсовет')),
                ('photo', models.TextField(blank=True, verbose_name='Фото')),
                ('contacts', models.TextField(blank=True, verbose_name='Контакты')),
                ('map_dormitory', models.TextField(blank=True, verbose_name='Карта')),
            ],
            options={
                'verbose_name': 'элемент раздела',
                'verbose_name_plural': "Раздел 'Об институте'",
            },
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_rules', models.TextField(blank=True, verbose_name='Правила приёма')),
                ('submit_doc', models.TextField(blank=True, verbose_name='Подать документы')),
                ('achievements', models.TextField(blank=True, verbose_name='Индивидуальные достижения')),
                ('special_rights', models.TextField(blank=True, verbose_name='Особые права и льготы')),
                ('admission_stat', models.TextField(blank=True, verbose_name='Статистика приёма')),
                ('enrollment_proc', models.TextField(blank=True, verbose_name='Порядок зачисления')),
            ],
            options={
                'verbose_name': 'элемент раздела',
                'verbose_name_plural': "Раздел 'Поступление'",
            },
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('bak', 'Бакалавриат'), ('spec', 'Специалитет'), ('mag', 'Магистратура')], default='bak', max_length=4, verbose_name='Уровень подготовки')),
                ('name_of_dir', models.CharField(max_length=100, verbose_name='Название специальности')),
                ('direction', models.CharField(max_length=10, unique=True, verbose_name='Код направления')),
                ('inf', models.TextField(verbose_name='Информация о специальности')),
            ],
            options={
                'verbose_name': 'элемент раздела',
                'verbose_name_plural': "Раздел 'Направления подготовки'",
                'ordering': ('level',),
            },
        ),
        migrations.CreateModel(
            name='Num_places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inf', models.TextField(blank=True, verbose_name='Информация о кол-ве мест')),
            ],
            options={
                'verbose_name': 'элемент раздела',
                'verbose_name_plural': "Раздел 'Поступление -> Количество мест'",
            },
        ),
        migrations.CreateModel(
            name='Passing_scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inf', models.TextField(blank=True, verbose_name='Информация о проходных баллах')),
            ],
            options={
                'verbose_name': 'элемент раздела',
                'verbose_name_plural': "Раздел 'Поступление -> Проходные баллы'",
            },
        ),
    ]