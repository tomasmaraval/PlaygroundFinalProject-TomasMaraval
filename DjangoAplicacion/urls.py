from django.shortcuts import render
from django.urls import path
from DjangoAplicacion.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

'''path('buscarPrecio/', buscarPrecio, name='buscarPrecio'),
    path('resultadoPrecio/', resultadoPrecio, name='resultadoPrecio'),'''

urlpatterns = [
    path('', inicio, name='inicio'),
    path('departamentos/', departamentos, name='deptos'),
    path('casas/', casas, name='casas'),
    path('dueños/', dueño, name='dueños'),
    
    path('buscar/', buscar_propiedades, name='buscar_propiedades'),

    path('casas/lista', CasaListView.as_view(), name='ListaCasas'),
    path('casas/crear', CasaCreateView.as_view(), name='CrearCasa'),
    path('casas/<pk>', CasaDetailView.as_view(), name='DetalleCasa'),
    path('casas/<pk>/editar', CasaUpdateView.as_view(), name='EditarCasa'),
    path('casas/<pk>/borrar', CasaDeleteView.as_view(), name='BorrarCasa'),

    path('dueños/lista', DueñoListView.as_view(), name='ListaDueños'),
    path('dueños/crear', DueñoCreateView.as_view(), name='CrearDueño'),
    path('dueños/<pk>', DueñoDetailView.as_view(), name='DetalleDueño'),
    path('dueños/<pk>/editar', DueñoUpdateView.as_view(), name='EditarDueño'),
    path('dueños/<pk>/borrar', DueñoDeleteView.as_view(), name='BorrarDueño'),

    path('departamentos/lista', DepartamentoListView.as_view(), name='ListaDepartamentos'),
    path('departamentos/crear', DepartamentoCreateView.as_view(), name='CrearDepartamento'),
    path('departamentos/<pk>', DepartamentoDetailView.as_view(), name='DetalleDepartamento'),
    path('departamentos/<pk>/editar', DepartamentoUpdateView.as_view(), name='EditarDepartamento'),
    path('departamentos/<pk>/borrar', DepartamentoDeleteView.as_view(), name='BorrarDepartamento'),

    path('login/', login_request, name='Login'),
    path('registro/', registro, name='Registro'),
    path('logout/', LogoutView.as_view(template_name='DjangoAplicacion/logout.html'), name='Logout'),
    path('editarPerfil/', editarPerfil, name='EditarPerfil'),
    path('cambiarContraseña', CambiarContraseña.as_view(), name='cambiarContraseña'),
] 
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)