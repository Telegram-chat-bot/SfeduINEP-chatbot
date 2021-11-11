from django.db import models

class Admission(models.Model):
    class Meta:
        verbose_name = "элемент раздела"
        verbose_name_plural = "Раздел 'Поступление'"
        
    admission_rules = models.TextField(
        verbose_name="Правила приёма",
        blank=True
        )
    submit_doc = models.TextField(
        verbose_name="Подать документы",
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
        return "Коллекция статей 'Поступление'"


class About(models.Model):
    class Meta:
        verbose_name = "элемент раздела"
        verbose_name_plural = "Раздел 'Об институте'"
    
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
        return "Коллекция статей 'Об институте'"
  
  
class Directions(models.Model):
    class Meta:
        verbose_name = "элемент раздела"
        verbose_name_plural = "Раздел 'Направления подготовки'"
        ordering = ['level', 'direction']
        # abstract = True
        
    levels = [
        ("bak", "Бакалавриат" ),
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
        verbose_name="Информация о специальности"
    )
    
    def __str__(self) -> str:
        return f"{self.level} - {self.direction}"
    
class Passing_scores(models.Model):
    class Meta:
        verbose_name = "элемент раздела"
        verbose_name_plural = "Раздел 'Поступление -> Проходные баллы'"

    inf = models.TextField(verbose_name="Информация о проходных баллах", blank=True)
    
    def __str__(self) -> str:
        return self.id
    
class Num_places(models.Model):
    class Meta:
        verbose_name = "элемент раздела"
        verbose_name_plural = "Раздел 'Поступление -> Количество мест'"
    
    inf = models.TextField(verbose_name="Информация о кол-ве мест", blank=True)