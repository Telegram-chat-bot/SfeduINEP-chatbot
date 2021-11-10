from django.db import models

class Admission(models.Model):
    class Meta:
        verbose_name_plural = "Раздел 'Поступление'"
        verbose_name = "Элемент раздела"
        
    admission_rules = models.TextField(
        verbose_name="Правила приёма",
        blank=True
        )
    submit_doc = models.TextField(
        verbose_name="Подать документы",
        blank=True
        )
    passing_scores= models.TextField(
        verbose_name="Проходные баллы",
        blank=True
        )
    number_of_places = models.TextField(
        verbose_name="Количество мест",
        blank=True
        )
    achievements = models.TextField(
        verbose_name="Индивидуальные достижения",
        blank=True
        )
    special_rights = models.TextField(
        verbose_name="Особые права и льготы",
        blank=True
        )
    admission_stat = models.TextField(
        verbose_name="Статистика приёма",
        blank=True
        )
    enrollment_proc = models.TextField(
        verbose_name="Порядок зачисления", 
        blank=True
        )
    
    def __str__(self) -> str:
        return "Статья"
    
class About(models.Model):
    class Meta:
        verbose_name_plural = "Раздел 'Об институте'"
        verbose_name = "Элемент раздела"
    
    acquaintance = models.TextField(
        verbose_name="Знакомство", 
        blank=True
        )
    excursion = models.TextField(
        verbose_name="Записаться на экскурсию", 
        blank=True
        )
    events = models.TextField(
        verbose_name="Мероприятия", 
        blank=True
        )
    science = models.TextField(
        verbose_name="Наука и учёба",
        blank=True
        )
    partners_work = models.TextField(
        verbose_name="Партнёры и трудоустройство",
        blank=True
        )
    stud_council = models.TextField(
        verbose_name="Студсовет", 
        blank=True
        )
    photo = models.TextField(
        verbose_name="Фото", 
        blank=True
        )
    contacts = models.TextField(
        verbose_name="Контакты",
        blank=True
        )
    map_dormitory = models.TextField(
        verbose_name="Карта", 
        blank=True
        )
    
    def __str__(self) -> str:
        return "Статья"
    
class Directions(models.Model):
    class Meta:
        verbose_name = "Элемент раздела"
        verbose_name_plural = "Раздел с направлениями подготовки"
    levels = [
        ("bak", "Бакалавриат" ),
        ("spec", "Специалитет"),
        ("mag", "Магистратура")
    ]
    blocks = [
        ("direct_of_prepare", "Направления подготовки"),
        ("passing_scores", "Проходные баллы"),
        ("num_of_places", "Количество мест"),
    ]
    
    level = models.CharField(
        max_length=4 ,
        verbose_name="Уровень подготовки", 
        choices=levels, 
        default="bak"
    )
    name_of_dir = models.CharField(
        max_length=100,
        verbose_name="Название специальности"
    )
    direction = models.CharField(max_length=10,
        verbose_name="Код направления"
    )
    section = models.CharField(max_length=20,
        verbose_name="Раздел бота",
        choices=blocks,
        default="direct_of_prepare"
    )
    inf = models.TextField(
        verbose_name="Информация о специальности"
    )
    
    def __str__(self) -> str:
        return f"({self.section}) {self.level} - {self.direction}"