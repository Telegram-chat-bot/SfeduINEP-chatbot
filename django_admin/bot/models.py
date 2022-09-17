from django.db import models
from django.db.models.deletion import CASCADE


class Page(models.Model):
    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "Разделы бота"
        app_label = "bot"
        ordering = ["row"]

    def get_file_path(self, filename):
        return f"{self.id}/{filename}"

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

    file = models.ImageField(
        verbose_name="Изображение",
        help_text="Изображение прикрепляется при необходимости",
        upload_to=get_file_path,
        null=True,
        blank=True,
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

    def get_file_path(self, filename):
        return f"{self.buttons_id}/{self.id}/{filename}"

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

    file = models.ImageField(
        verbose_name="Изображение",
        help_text="Изображение прикрепляется при необходимости",
        upload_to=get_file_path,
        null=True,
        blank=True,
        default=None
    )

    inline_tag = models.CharField(
        verbose_name="Идентификатор кнопки",
        max_length=20,
        help_text="Для разработчиков",
        blank=True
    )

    def __str__(self):
        return f"Кнопка {self.btn_title}"


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
