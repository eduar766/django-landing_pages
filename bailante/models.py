from django.db import models

# Create your models here.
class MensajeBailante(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models. CharField(max_length=20)

    def __str__(self):
        return 'Lead: {}, ID: {}'.format(self.name, self.id)
