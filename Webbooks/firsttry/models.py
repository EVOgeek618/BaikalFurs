from django.db import models

class Photo(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    dir_way = models.FileField(upload_to="static/image/photo/")
