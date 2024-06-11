from django.db import models
from django.utils import timezone
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    imagen = models.URLField(verbose_name="URL del logo")
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre