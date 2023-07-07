from django.db import models
from .data import CLASS_CHOICES, PREDMET_CHOICES

class Student(models.Model):
    login = models.CharField("Логін учня", max_length=15, unique=True)
    clas = models.CharField("Клас", max_length=4, choices=CLASS_CHOICES)
    last_name = models.CharField("Ім'я учня", max_length=20)
    first_name = models.CharField("Прізвище учня", max_length=20)
    image = models.ImageField('Аватарка учня', upload_to='D:\Working\Praktic\Project\Diary\student\static\student\img')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = "Учень"
        verbose_name_plural = "Учні"
class Teacher(models.Model):
    login = models.CharField("Логін вчителя", max_length=15, unique=True)
    last_name = models.CharField("Ім'я вчителя", max_length=15)
    first_name = models.CharField("Прізвище вчителя", max_length=15)
    predmet = models.CharField("Предмети", max_length=255, choices=PREDMET_CHOICES)
    head_clas = models.CharField("Керівние класу", max_length=5, default='Немає', choices=tuple([('Немає', 'Немає')]+list(CLASS_CHOICES)))
    image = models.ImageField('Аватарка вчителя', upload_to='D:\Working\Praktic\Project\Diary\\teacher\static\\teacher\img')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = "Вчитель"
        verbose_name_plural = "Вчителі"
