from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    titulo = models.CharField(max_length= 50)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fechapost = models.DateField(auto_now_add=True)
    categorias = models.CharField(max_length= 50, default='Otros')
    imagen = models.ImageField(null=True, blank=True, upload_to = "imagenes/")

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('articulodetalle', args=[str(self.id)])
