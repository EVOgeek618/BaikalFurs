from django.contrib import admin
from .models import Photo,Ask,Otchets,URL_Video, Comment, Forum_Topic
@admin.register(Otchets)
class AdminPhoto(admin.ModelAdmin):
    list_display = ("id","name", "date", "text")
@admin.register(Photo)
class AdminFile(admin.ModelAdmin):
    list_display = ("name", "dir_way", "otchet", "is_video")
@admin.register(Ask)
class AdminAsk(admin.ModelAdmin):
    list_display = ("name", "email", "date", "quetion")
@admin.register(URL_Video)
class AdminOtchet(admin.ModelAdmin):
    list_display = ("name", "dir_way", "otchet")
@admin.register(Forum_Topic)
class AdminTopic(admin.ModelAdmin):
    list_display = ("id", "title", "theme", "start_data", "user", "text")
@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ("id", "topic", "data", "user", "text", "quetion")
