"""Webbooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Webbooks.firsttry import views
urlpatterns = [
    path('', views.home),
    path('faq/', views.faq),
    path('contacts/', views.contacts),
    path('forum/', views.forum),
    path('forum/add/<int:stheme>/', views.add_forum_theme),
    path('forum/add/', views.add_forum_theme),
    path('forum/theme/<str:theme>', views.forum),
    path('forum/<int:id>/', views.topic),
    path('photoarchive/', views.photo),
    path('products/', views.products),
    path('otchet/<str:name>/', views.otchet),
    path('admin/', admin.site.urls),
]
