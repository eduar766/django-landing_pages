from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gracias/', views.gracias, name='gracias'),
    path('send/', views.sendEmail, name='send'),
]
