from django.shortcuts import render, redirect, get_object_or_404
from DjangoAplicacion.models import *
from django.http import HttpResponse
from django.template import loader
from DjangoAplicacion.forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request, "DjangoAplicacion/inicio.html")

def index(request):
    return render(request, "DjangoAplicacion/index.html")

def padre(request):
    return render(request, "DjangoAplicacion/padre.html")


def dueño(request):
    current_user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form = DueñoFormulario(request.POST)
        if form.is_valid():
            dueño = form.save(commit=False)
            dueño.user = current_user
            dueño.save()
            messages.success(request, 'Dueño creado correctamente')
            return redirect('DjangoAplicacion/inicio.html')
        else:
            messages.error(request, 'Error al crear el dueño')
            form = DueñoFormulario()
        return render(request, 'DjangoAplicacion/dueño.html', {'form': form})

        

    """if request.method == 'POST':
        mi_formulario = DueñoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            dueño = Dueño(user = informacion['user'], nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            dueño.save()
            return render(request, "DjangoAplicacion/inicio.html")
    else:
        mi_formulario = DueñoFormulario()
        return render(request, "DjangoAplicacion/dueño.html", {"mi_formulario": mi_formulario})"""

def casas(request):
    current_user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form = CasaFormulario(request.POST)
        if form.is_valid():
            casa = form.save(commit=False)
            casa.user = current_user
            casa.save()
            messages.success(request, 'Casa publicada correctamente')
            return redirect('DjangoAplicacion/inicio.html')
        else:
            messages.error(request, 'Error al publicar')
            form = CasaFormulario()
        return render(request, 'DjangoAplicacion/casa.html', {'form': form})

def departamentos(request):
    current_user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form = DepartamentoFormulario(request.POST)
        if form.is_valid():
            departamento = form.save(commit=False)
            departamento.user = current_user
            departamento.save()
            messages.success(request, 'Depto publicado correctamente')
            return redirect('DjangoAplicacion/inicio.html')
        else:
            messages.error(request, 'Error al publicar')
            form = DepartamentoFormulario()
        return render(request, 'DjangoAplicacion/deptos.html', {'form': form})

'''def buscarPrecio(request):
    return render(request, "DjangoAplicacion/buscarPrecio.html")

def resultadoPrecio(request):
    if request.GET['precio']:
        precio = request.GET['precio'] 
        direccion = Departamento.objects.filter(precio=precio)
        return render(request, 'DjangoAplicacion/resultadosPrecio.html', {'precio': precio, 'direccion': direccion})
    
    return render(request, 'DjangoAplicacion/inicio.html')'''

def buscar_propiedades(request):
    if request.method == 'POST':
        precio_input = request.POST.get('precio', None)
        if precio_input is not None:
            try:
                precio = int(precio_input)
                departamentos = Departamento.objects.filter(precio__gte=precio - 10000, precio__lte=precio + 10000)
                casas = Casa.objects.filter(precio__gte=precio - 10000, precio__lte=precio + 10000)
                propiedades = list(departamentos) + list(casas)
                return render(request, 'DjangoAplicacion/resultado_busqueda.html', {'propiedades': propiedades})
            
            except ValueError:
                mensaje_error = "Ingrese un precio válido."
                return render(request, 'DjangoAplicacion/buscador.html', {'mensaje_error': mensaje_error})

    return render(request, 'DjangoAplicacion/buscador.html')


class DepartamentoListView(ListView):
    model = Departamento
    context_object_name = 'departamentos'
    template_name = 'DjangoAplicacion/departamento_listas.html'

class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = 'DjangoAplicacion/departamento_detalle.html'

class DepartamentoCreateView(CreateView):
    model = Departamento
    template_name = 'DjangoAplicacion/departamento_crear.html'
    success_url = reverse_lazy('ListaDepartamentos')
    fields = ['direccion', 'piso', 'departamento', 'ambientes', 'metros_cuadrados', 'precio', 'imagen']

class DepartamentoUpdateView(UpdateView):
    model = Departamento
    template_name = 'DjangoAplicacion/departamento_editar.html'
    success_url = reverse_lazy('ListaDepartamentos')
    fields = ['direccion', 'piso', 'departamento', 'ambientes', 'metros_cuadrados', 'precio', 'imagen']

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = 'DjangoAplicacion/departamento_borrar.html'
    success_url = reverse_lazy('ListaDepartamentos')


class CasaListView(ListView):
    model = Casa
    context_object_name = 'casas'
    template_name = 'DjangoAplicacion/casa_listas.html'

class CasaDetailView(DetailView):
    model = Casa
    template_name = 'DjangoAplicacion/casa_detalle.html'

class CasaCreateView(CreateView):
    model = Casa
    template_name = 'DjangoAplicacion/casa_crear.html'
    success_url = reverse_lazy('ListaCasas')
    fields = ['direccion', 'ambientes', 'metros_cuadrados', 'precio', 'imagen']

class CasaUpdateView(UpdateView):
    model = Casa
    template_name = 'DjangoAplicacion/casa_editar.html'
    success_url = reverse_lazy('ListaCasas')
    fields = ['direccion', 'ambientes', 'metros_cuadrados', 'precio', 'imagen']

class CasaDeleteView(DeleteView):
    model = Casa
    template_name = 'DjangoAplicacion/casa_borrar.html'
    success_url = reverse_lazy('ListaCasas')


class DueñoListView(ListView):
    model = Dueño
    context_object_name = 'dueños'
    template_name = 'DjangoAplicacion/dueño_listas.html'

class DueñoDetailView(DetailView):
    model = Dueño
    template_name = 'DjangoAplicacion/dueño_detalle.html'

class DueñoCreateView(CreateView):
    model = Dueño
    template_name = 'DjangoAplicacion/dueño_crear.html'
    success_url = reverse_lazy('ListaDueños')
    fields = ['nombre', 'apellido', 'email']

class DueñoUpdateView(UpdateView):
    model = Dueño
    template_name = 'DjangoAplicacion/dueño_editar.html'
    success_url = reverse_lazy('ListaDueños')
    fields = ['nombre', 'apellido', 'email']

class DueñoDeleteView(DeleteView):
    model = Dueño
    template_name = 'DjangoAplicacion/dueño_borrar.html'
    success_url = reverse_lazy('ListaDueños')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasena)
            if user is not None:
                login(request, user)
                return render(request, "DjangoAplicacion/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "DjangoAplicacion/inicio.html", {"mensaje": "Datos incorrectos"})
    else:
        form = AuthenticationForm()

    return render(request, "DjangoAplicacion/login.html", {"form": form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "DjangoAplicacion/inicio.html", {"mensaje": f"Usuario {username} creado"})
    else:
        form = UserCreationFormCustom()
    return render(request, "DjangoAplicacion/registro.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if mi_formulario.cleaned_data.get['imagen']:
                usuario.imagen = mi_formulario.cleaned_data['imagen']
            usuario.save()
            return render(request, "DjangoAplicacion/inicio.html")
        
    else:
        mi_formulario = UserEditForm(instance=request.user)
    return render(request, "DjangoAplicacion/editarPerfil.html", {"mi_formulario":mi_formulario})

class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = 'DjangoAplicacion/cambiarContraseña.html'
    success_url = reverse_lazy('EditarPerfil')
    