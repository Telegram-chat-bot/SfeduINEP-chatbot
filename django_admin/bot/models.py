from django.db import models
from django.db.models.deletion import CASCADE


class Page(models.Model):
    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "Разделы бота"
        app_label = "bot"
        ordering = ["row"]

    def get_file_path(instance, filename):
        return f"{instance.id}/{filename}"

    btn_title = models.CharField(
        verbose_name="Название раздела",
        max_length=50
    )
    inline_tag = models.CharField(
        verbose_name="Идентификатор инлайн меню",
        max_length=25,
        blank=True,
        default=""
    )
    row = models.PositiveSmallIntegerField(
        verbose_name="Номер ряда в клавиатуре",
        help_text="Только положительные числа",
        default=1
    )

    file = models.FileField(
        verbose_name="Изображение или другой файл",
        help_text="Файл приклепляется при необходимости",
        upload_to=get_file_path,
        null=True,
        default=None
    )

    def __str__(self):
        return f"Кнопка '{self.btn_title}'"


class InfoPage(models.Model):
    class Meta:
        verbose_name = "поле"
        verbose_name_plural = "Поля"
        app_label = "bot"

    type_field = [
        ("comment", "Комментарий к кнопке"),
        ("keyboard", "Инлайн клавиатура (Клавиатура с направлениями)"),
        ("info", "Информация раздела"),
        ("none", "Без типа")
    ]

    fields = models.ForeignKey(
        Page,
        on_delete=CASCADE
    )

    type_content = models.CharField(
        verbose_name="Тип контента",
        max_length=30,
        choices=type_field,
        help_text="""
Выбор 'Без типа' означает, что кнопка должна иметь специфическое программирование, отличное от остальных кнопок'
"""

    )

    info = models.TextField(
        verbose_name="Информация",
        blank=True
    )

    def __str__(self):
        return f"Поле '{self.type_content}'"


class InnerKeyboard(models.Model):
    class Meta:
        verbose_name = "Кнопка"
        verbose_name_plural = "Вложенная клавиатура"
        app_label = "bot"

    def get_file_path(instance, filename):
        return f"{instance.buttons_id}/{instance.id}/{filename}"

    row = models.PositiveSmallIntegerField(
        verbose_name="Номер ряда в клавиатуре",
        help_text="Только положительные числа",
        default=1
    )

    buttons = models.ForeignKey(
        Page, on_delete=CASCADE
    )

    btn_title = models.CharField(
        verbose_name="Имя кнопки",
        max_length=50
    )
    type_content = models.CharField(
        verbose_name="Тип контента",
        max_length=30,
        choices=InfoPage.type_field
    )
    info = models.TextField(
        verbose_name="Информация",
        blank=True
    )

    file = models.FileField(
        verbose_name="Изображение или другой файл",
        help_text="Файл приклепляется при необходимости",
        upload_to=get_file_path,
        null=True,
        blank=True
    )

    inline_tag = models.CharField(
        verbose_name="Идентификатор кнопки",
        max_length=20,
        help_text="Для разработчиков",
        blank=True
    )

    def __str__(self):
        return f"Кнопка {self.btn_title}"


# class Admission(models.Model):
#     class Meta:
#         verbose_name = "элемент раздела"
#         verbose_name_plural = "Раздел 'Поступление'"
#         app_label = "bot"
#
#     admission_rules = models.TextField(
#         verbose_name="Правила приёма",
#         blank=True
#     )
#     submit_doc = models.TextField(
#         verbose_name="Подать документы",
#         blank=True
#     )
#     achievements = models.TextField(
#         verbose_name="Индивидуальные достижения",
#         blank=True
#     )
#     special_rights = models.TextField(
#         verbose_name="Особые права и льготы",
#         blank=True
#     )
#     admission_stat = models.TextField(
#         verbose_name="Статистика приёма",
#         blank=True
#     )
#     enrollment_proc = models.TextField(
#         verbose_name="Порядок зачисления",
#         blank=True
#     )
#
#     def __str__(self) -> str:
#         return "Коллекция статей 'Поступление'"


# class About(models.Model):
#     class Meta:
#         verbose_name = "элемент раздела"
#         verbose_name_plural = "Раздел 'Об институте'"
#         app_label = "bot"
#
#     acquaintance = models.TextField(
#         verbose_name="Знакомство",
#         blank=True
#     )
#     excursion = models.TextField(
#         verbose_name="Записаться на экскурсию",
#         blank=True
#     )
#     events = models.TextField(
#         verbose_name="Мероприятия",
#         blank=True
#     )
#     science = models.TextField(
#         verbose_name="Наука и учёба",
#         blank=True
#     )
#     partners_work = models.TextField(
#         verbose_name="Партнёры и трудоустройство",
#         blank=True
#     )
#     stud_council = models.TextField(
#         verbose_name="Студсовет",
#         blank=True
#     )
#     photo = models.TextField(
#         verbose_name="Фото",
#         blank=True
#     )
#     contacts = models.TextField(
#         verbose_name="Контакты",
#         blank=True
#     )
#     map_dormitory = models.TextField(
#         verbose_name="Карта",
#         blank=True
#     )
#
#     def __str__(self) -> str:
#         return "Коллекция статей 'Об институте'"


class Directions(models.Model):
    class Meta:
        verbose_name = "элемент раздела"
        verbose_name_plural = "Раздел 'Направления подготовки'"
        ordering = ['level', 'direction']
        app_label = "bot"

    levels = [
        ("bak", "Бакалавриат"),
        ("spec", "Специалитет"),
        ("mag", "Магистратура")
    ]

    level = models.CharField(
        max_length=4,
        verbose_name="Уровень подготовки",
        choices=levels,
        default=levels[0][0]
    )
    name_of_dir = models.CharField(
        max_length=100,
        verbose_name="Название специальности"
    )
    direction = models.CharField(max_length=10,
                                 verbose_name="Код направления",
                                 unique=True
                                 )
    inf = models.TextField(
        verbose_name="Информация о специальности",
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.level} - {self.direction}"


class Passing_scores(models.Model):
    class Meta:
        verbose_name = "Проходные баллы"
        verbose_name_plural = "Информация о проходных баллах'"
        ordering = ["direction"]
        app_label = "bot"

    direction = models.OneToOneField(
        "Directions",
        on_delete=CASCADE,
        null=True,
        unique=True,
        verbose_name="Направление подготовки"
    )
    inf = models.TextField(verbose_name="Информация о проходных баллах", blank=True)

    def __str__(self):
        return f"{self.direction}"


class Num_places(models.Model):
    class Meta:
        verbose_name = "Количество мест"
        verbose_name_plural = "Информация о количестве мест'"
        ordering = ["direction"]
        app_label = "bot"

    direction = models.OneToOneField(
        'Directions',
        on_delete=CASCADE,
        verbose_name="Направление подготовки",
        unique=True,
        null=True
    )
    inf = models.TextField(verbose_name="Информация о кол-ве мест", blank=True)

    def __str__(self):
        return f"{self.direction}"


# class Questions(models.Model):
#     class Meta:
#         verbose_name = "элемент раздела"
#         verbose_name_plural = "Раздел 'Задать вопрос'"
#         app_label = "bot"
#
#     faq = models.TextField(
#         verbose_name="F.A.Q",
#         blank=True
#     )
#
#     def __str__(self) -> str:
#         return "Часто задаваемые вопросы"


class Welcome_message(models.Model):
    class Meta:
        verbose_name = "приветствие"
        verbose_name_plural = "Приветствие бота"
        app_label = "bot"

    message = models.TextField(
        verbose_name="Текст приветствия"
    )

    def __str__(self) -> str:
        return "Текст приветствия"


class Help_content(models.Model):
    class Meta:
        verbose_name = "содержимое раздела 'Помощь'"
        verbose_name_plural = "Раздел 'Помощь'"
        app_label = "bot"

    type_user = [
        ("supergroup", "Группа"),
        ("private", "Абитуриенты")
    ]
    target_user = models.CharField(
        verbose_name="Целевой раздел",
        choices=type_user,
        max_length=11,
        help_text="Выберите, для кого нацелены инструкции (Сотрудники ИНЭП или абитуриенты)"
    )
    content = models.TextField(
        verbose_name="Содержимое раздела 'Помощь'",
        blank=True
    )

    def __str__(self) -> str:
        return f"Раздел 'Помощь' для {'групп' if self.target_user == 'supergroup' else 'абитуриентов'}"
