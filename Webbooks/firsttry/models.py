from django.db import models

class Photo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название отчёта")
    date = models.DateField(verbose_name="Дата загрузки")
    dir_way = models.FileField(upload_to="static/image/photo/", verbose_name="Файл")
    is_video = models.BooleanField(verbose_name="Видео?")