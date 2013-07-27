from django.db import models

class Cinema(models.Model):
    name = models.CharField(verbose_name=u"Название", max_length=60)
    address = models.TextField(verbose_name=u"Адрес")

class Presentation(models.Model):
    cinema = models.ForeignKey(Cinema, verbose_name=u"Кинотеатр")
    time = models.DateTimeField(verbose_name=u"Дата и время показа")
    film = models.TextField(verbose_name=u"Фильм")