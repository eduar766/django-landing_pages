from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('servicios', views.servicios, name='servicios'),
    path('como-reciclar', views.como_reciclar, name='como_reciclar'),
    path('galeria', views.galeria, name='galeria'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('send', views.sendForm, name='send'),
    path('carga', views.cargaFoto, name='carga'),
    path('sendImg', views.upload, name='sendImg'),
]
