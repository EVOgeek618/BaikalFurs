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
    user = models.CharField(max_length=50, verbose_name="Имя отправителя", null=True)
    quetion = models.TextField(verbose_name="Вопрос")

class Forum_Topic(models.Model):
    title = models.CharField(max_length=100, verbose_name="Тема обсуждения")
    theme = models.CharField(max_length=100, verbose_name="Принадлежность к теме форума")
    start_data = models.DateTimeField(verbose_name="Дата создания обсуждения")
    user = models.CharField(max_length=30, verbose_name="Автор топика", default="Анонимный охотник")
    text = models.TextField(verbose_name="Разъяснение обсуждения")
    def __str__(self):
        return self.title

class Comment(models.Model):
    topic = models.ForeignKey(Forum_Topic, on_delete=models.CASCADE, verbose_name="Принадлежность к обсуждению")
    data = models.DateTimeField(verbose_name="Дата создания обсуждения")
    user = models.CharField(max_length=30, verbose_name="Автор комментария", default="Анонимный охотник")
    text = models.TextField(verbose_name="Текст комментария")
    quetion = models.IntegerField(verbose_name="Номер комментария-вопроса", blank=True, null=True)