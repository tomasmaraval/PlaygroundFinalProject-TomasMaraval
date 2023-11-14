from django.shortcuts import render, redirect
from DjangoAplicacion.models import *
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "DjangoAplicacion/inicio.html")

def index(request):
    return render(request, "DjangoAplicacion/index.html")

def padre(request):
    return render(request, "DjangoAplicacion/padre.html")

def profesores(request):
    return render(request, "DjangoAplicacion/profesores.html")

def estudiantes(request):
    return render(request, "DjangoAplicacion/estudiantes.html")

def entregables(request):
    return render(request, "DjangoAplicacion/entregables.html")

def cursos(request):
    if request.method == 'POST':
        curso_nombre = request.POST.get("curso")
        camada = request.POST.get("camada")
        
        Curso.objects.create(curso=curso_nombre, camada=camada)
        
        return render(request, "DjangoAplicacion/inicio.html")
    else:
        return render(request, "DjangoAplicacion/cursos.html")

def buscarCamada(request):
    return render(request, "DjangoAplicacion/buscarCamada.html")

def buscar(request):
    if "camada" in request.GET:
        camada = request.GET["camada"]
        curso = Curso.objects.filter(camada_conteins=camada)
        return render(request, 'DjangoAplicacion/resultadosBusqueda.html', {'cursos': curso, 'camada': camada})
                      
    
    else:
        return render(request, 'DjangoAplicacion/buscar.html')
    
