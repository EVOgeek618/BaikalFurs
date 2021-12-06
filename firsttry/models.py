from django.db import models
from django.contrib.auth.models import User

class Otchets(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название отчёта")
    date = models.DateField(verbose_name="Дата загрузки")
    text = models.TextField(verbose_name="Текст отчета")
    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название фото/видео", null=True, default="Неизвестное")
    dir_way = models.FileField(upload_to="images/", verbose_name="Файл")
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор топика")
    text = models.TextField(verbose_name="Разъяснение обсуждения")
    ava = models.FileField(upload_to="profiles/", default='profiles/ava.jpg')
    def __str__(self):
        return self.title

class Comment(models.Model):
    topic = models.ForeignKey(Forum_Topic, on_delete=models.CASCADE, verbose_name="Принадлежность к обсуждению")
    data = models.DateTimeField(verbose_name="Дата создания обсуждения")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    text = models.TextField(verbose_name="Текст комментария")
    quetion = models.IntegerField(verbose_name="Номер комментария-вопроса", blank=True, null=True)
    ava = models.FileField(upload_to="profiles/", default='profiles/ava.jpg')

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    firstname = models.CharField(max_length=40, verbose_name="Имя", blank=True, null=True, default='')
    lastname = models.CharField(max_length=40, verbose_name="Фамилия", blank=True, null=True, default='')
    info = models.TextField(verbose_name="О себе", blank=True, null=True, default='')
    sex = models.BooleanField(verbose_name="Мужчина?", null=True, blank=True)
    ava = models.FileField(upload_to="profiles/", default='profiles/ava.jpg', verbose_name="Аватарка")

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
