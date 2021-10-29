from django.contrib import admin
from .models import Photo,Ask,Otchets,URL_Video
@admin.register(Otchets)
class AdminPhoto(admin.ModelAdmin):
    list_display = ("name", "date", "text")
@admin.register(Photo)
class AdminAsk(admin.ModelAdmin):
    list_display = ("name", "dir_way", "otchet", "is_video")
@admin.register(Ask)
class AdminAsk(admin.ModelAdmin):
    list_display = ("name", "email", "date", "quetion")
@admin.register(URL_Video)
class AdminAsk(admin.ModelAdmin):
    list_display = ("name", "dir_way", "otchet")

# Register your models here.
