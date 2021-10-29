from django.db import models

class Otchets(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название отчёта")
    date = models.DateField(verbose_name="Дата загрузки")
    text = models.TextField(verbose_name="Текст отчета")
    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название фото/видео", null=True, default="Неизвестное")
    dir_way = models.FileField(upload_to="static/image/photo/", verbose_name="Файл")
    otchet = models.ForeignKey(Otchets, on_delete=models.CASCADE, verbose_name="Название отчёта")
    is_video = models.BooleanField(verbose_name="Видео?")

class URL_Video(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название фото/видео", null=True, default="Неизвестное")
    dir_way = models.URLField(verbose_name="Ссылка на видео")
    otchet = models.ForeignKey(Otchets, on_delete=models.CASCADE, verbose_name="Название отчёта")

class Ask(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тема вопроса")
    date = models.DateTimeField(verbose_name="Дата загрузки")
    email = models.EmailField(verbose_name="Почта отправителя")
    quetion = models.TextField(verbose_name="Вопрос")
