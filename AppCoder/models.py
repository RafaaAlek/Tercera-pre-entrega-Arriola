from django.db import models

# Create your models here.
class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()


class Cliente(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()


class Categoria(models.Model):

    nombre = models.CharField(max_length=30)
    
