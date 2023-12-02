<<<<<<< HEAD
from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Departamento (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='departamentos')
    direccion = models.CharField(max_length=40, null=False)
    piso = models.IntegerField(null=False)
    departamento = models.CharField(max_length=40, null=False)
    ambientes = models.IntegerField(null=False)
    metros_cuadrados  = models.IntegerField(null=False)
    precio = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    imagen = models.ImageField(default='5411.jpeg', upload_to='departamentos', null=True, blank=True)

    def __str__(self) -> str:
        return f'Usuario: @{self.user}, Direccion: {self.direccion}, Piso: {self.piso}, Departamento: {self.departamento}, Ambientes: {self.ambientes}, Metros Cuadrados: {self.metros_cuadrados}, Precio: {self.precio}, {self.imagen}'

class Casa (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='casas')
    direccion = models.CharField(max_length=40, null=False, default='')
    ambientes = models.IntegerField(null=False)
    metros_cuadrados  = models.IntegerField(null=False)
    precio = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    imagen = models.ImageField(default='5411.jpeg', upload_to='casas', null=True, blank=True)

    def __str__(self) -> str:
        return f'Usuario: @{self.user}, Direccion: {self.direccion}, Ambientes: {self.ambientes}, Metros Cuadrados: {self.metros_cuadrados}, Precio: {self.precio}, {self.imagen}'

class Dueño (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="dueños")
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=False)

    def __str__(self) -> str:
        return f'Usuario: @{self.user}, Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}'

class Avatar (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    imagen = models.ImageField(default='5411.jpeg', upload_to='avatares', null=True, blank=True)

    def __str__(self) -> str:
        return f'Avatar de: @{self.user}'
    
class Usuario (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return f'Usuario: @{self.user}'
=======
from django.db import models

# Create your models here.
class Curso (models.Model):
    curso = models.CharField(max_length=40)
    camada = models.IntegerField()

class Profesor (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Estudiante (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Entregable (models.Model):
    nombre = models.CharField(max_length=30)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
>>>>>>> origin/main
