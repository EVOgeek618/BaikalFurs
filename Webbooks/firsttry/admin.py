from django.contrib import admin
from .models import Photo
@admin.register(Photo)
class AdminPhoto(admin.ModelAdmin):
    list_display = ("name", "date", "dir_way", "is_video")
# Register your models here.
