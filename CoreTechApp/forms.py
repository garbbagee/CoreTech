# forms.py

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'imagen']

from django.contrib.auth.models import User

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Nuevo nombre de usuario'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nuevo nombre de usuario'})
        }
        help_texts = {
            'username': '150 caracteres o menos. Solo letras, dígitos y @/./+/-/_ están permitidos.'
        }
        error_messages = {
            'username': {
                'required': 'Por favor, ingrese un nombre de usuario.',
                'unique': 'Este nombre de usuario ya está en uso. Elija otro.',
            },
        }