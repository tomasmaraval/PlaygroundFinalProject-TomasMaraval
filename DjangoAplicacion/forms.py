from django import forms
from .models import Departamento, Casa, Dueño
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserModel, UserChangeForm

class DepartamentoFormulario(forms.Form):
    direccion = forms.CharField()
    piso = forms.IntegerField()
    departamento = forms.CharField()
    ambientes = forms.IntegerField()
    metros_cuadrados = forms.IntegerField()
    precio = forms.IntegerField()
    imagen = forms.ImageField(label='Ingrese la foto del departamento: ')

    class Meta:
        model = Dueño
        fields = ("direccion", "piso", "departamento", "ambientes", "metros_cuadrados", "precio", "imagen")

class CasaFormulario(forms.Form):
    direccion = forms.CharField()
    ambientes = forms.IntegerField()
    metros_cuadrados = forms.IntegerField()
    precio = forms.IntegerField()
    imagen = forms.ImageField(label='Ingrese la foto de la casa: ')

    class Meta:
        model = Dueño
        fields = ("direccion", "ambientes", "metros_cuadrados", "precio", "imagen")

class DueñoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = Dueño
        fields = ("nombre", "apellido", "email")

class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label='Usuario', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k: '' for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Ingrese su email:')
    first_name = forms.CharField(label='Ingrese su nombre:')
    last_name = forms.CharField(label='Ingrese su apellido:')
    imagen = forms.ImageField(label='Ingrese su foto de perfil:', required=False)

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'imagen')
        help_texts = {k: '' for k in fields}