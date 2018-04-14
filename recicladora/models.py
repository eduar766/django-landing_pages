from django.db import models

# Create your models here.
class RecicladoraMensaje(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()

    def __str__(self):
        return 'Lead: {}, Email: {}'.format(self.name, self.email)

class Galeria(models.Model):
    name = models.CharField(max_length=100)
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.name
