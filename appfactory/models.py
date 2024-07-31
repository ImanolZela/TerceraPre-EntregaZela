from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}" 