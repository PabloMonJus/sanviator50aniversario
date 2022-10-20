from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Noticia(models.Model):
    title= models.CharField(max_length=200,verbose_name="Título")
    descripcion=models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen",upload_to="noticias")
    created= models.TimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    updated=models.TimeField(auto_now=True,verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural= "Noticias"
        ordering=["-created"]

    def __str__(self):
        return self.title
