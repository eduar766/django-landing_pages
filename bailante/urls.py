from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('carousel/', views.carousel, name='carousel'),
    path('send/', views.sendForm, name='send')
]
