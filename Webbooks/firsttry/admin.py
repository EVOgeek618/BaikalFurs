from django.contrib import admin
from .models import Photo,Ask,Otchets
@admin.register(Otchets)
class AdminPhoto(admin.ModelAdmin):
    list_display = ("name", "date", "text")
@admin.register(Photo)
class AdminAsk(admin.ModelAdmin):
    list_display = ("name", "dir_way", "otchet", "is_video")
@admin.register(Ask)
class AdminAsk(admin.ModelAdmin):
    list_display = ("name", "email", "date", "quetion")

# Register your models here.
