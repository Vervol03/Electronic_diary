from django.db import models
from .data import CLASS_CHOICES, PREDMET_CHOICES
from main.models import Student


class Rozk(models.Model):
    clas = models.CharField("Клас", max_length=4, choices=CLASS_CHOICES, unique=True)
    Monday = models.TextField("Понеділок", max_length=255, default="")
    Tuesday = models.TextField("Вівторок", max_length=255, default="")
    Wednesday = models.TextField("Середа", max_length=255, default="")
    Thursday = models.TextField("Четверг", max_length=255, default="")
    Friday = models.TextField("П'ятниця", max_length=255, default="")

    def __str__(self):
        return self.clas

    class Meta:
        verbose_name = "Розклад класу"
        verbose_name_plural = "Розклади класів"


class Work(models.Model):
    clas = models.CharField("Клас", max_length=4, choices=CLASS_CHOICES)
    predmet = models.CharField("Предмет", max_length=255, choices=PREDMET_CHOICES)
    work = models.CharField("Завдання", max_length=255, default="", blank=True)

    def __str__(self):
        return self.clas+'_'+self.predmet

    class Meta:
        verbose_name = "Завдання класу"
        verbose_name_plural = "Завдання класів"


class Estimates(models.Model):
    login = models.ForeignKey(Student, on_delete=models.CASCADE)
    predmet = models.CharField("Предмет", max_length=255, choices=PREDMET_CHOICES)
    estimate = models.CharField("Оцінки", max_length=255, default="", blank=True)

    def __str__(self):
        return str(self.login)+'_'+self.predmet

    class Meta:
        verbose_name = "Оцінки учня"
        verbose_name_plural = "Оцінки учнів"

