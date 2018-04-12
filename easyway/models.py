from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class EnviarMensaje(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    hora = models.DateTimeField('date published')

    def __str__(self):
        return 'Lead: {}, ID: {}'.format(self.name, self.id)

class EnviarMensajeTwo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    hora = models.CharField(max_length=80)

    def __str__(self):
        return 'Lead: {}, ID: {}'.format(self.name, self.id)
