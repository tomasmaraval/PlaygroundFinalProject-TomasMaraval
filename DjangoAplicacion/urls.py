from django.shortcuts import render
from django.urls import path
from DjangoAplicacion.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profes'),
    path('estudiantes/', estudiantes, name='alumnos'),
    path('entregables/', entregables, name='entregables'),
    path('buscar/', buscar, name='buscar'),
]