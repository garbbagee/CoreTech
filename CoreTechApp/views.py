from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.http import HttpResponse
import json
from .forms import ProductoForm, Producto

def index(request):
    return render(request, 'html/index.html')

def acercade(request):
    return render(request, 'html/acercade.html')

def carrocompras(request):
    return render(request, 'html/carrocompras.html')

def cuenta(request):
    return render(request, 'html/cuenta.html')

def gama_alta(request):
    return render(request, 'html/GamaAlta.html')

def gama_media(request):
    return render(request, 'html/GamaMedia.html')

def gama_baja(request):
    return render(request, 'html/GamaBaja.html')

# Agregar las vistas para los otros archivos HTML
def torrega1(request):
    return render(request, 'html/torrega1.html')

def torrega2(request):
    return render(request, 'html/torrega2.html')

def torrega3(request):
    return render(request, 'html/torrega3.html')

def torrega4(request):
    return render(request, 'html/torrega4.html')

def torregb1(request):
    return render(request, 'html/torregb1.html')

def torregb2(request):
    return render(request, 'html/torregb2.html')

def torregb3(request):
    return render(request, 'html/torregb3.html')

def torregb4(request):
    return render(request, 'html/torregb4.html')

def torregm1(request):
    return render(request, 'html/torregm1.html')

def torregm2(request):
    return render(request, 'html/torregm2.html')

def torregm3(request):
    return render(request, 'html/torregm3.html')

def torregm4(request):
    return render(request, 'html/torregm4.html')


#Función pal registro e inicio de sesión

def register(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        username = request.POST.get('user')
        telefono = request.POST.get('fono')
        email = request.POST.get('email')
        password = request.POST.get('contra')

        # Validaciones de campos
        if not nombre or not username or not telefono or not email or not password:
            return JsonResponse({"status": "error", "message": "Todos los campos son obligatorios."})

        if len(password) < 8:
            return JsonResponse({"status": "error", "message": "La contraseña debe tener al menos 8 caracteres."})

        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": "error", "message": "El nombre de usuario ya está en uso."})

        if User.objects.filter(email=email).exists():
            return JsonResponse({"status": "error", "message": "El correo electrónico ya está en uso."})

        # Crear el usuario
        user = User.objects.create_user(username=username, first_name=nombre, email=email, password=password)
        user.save()

        # Autenticar y redirigir al usuario
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Cuenta creada para {username}!')
            return JsonResponse({"status": "success", "message": "Registro exitoso.", "redirect": "index"})

    return render(request, 'cuenta.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('correo2')
        password = request.POST.get('contra2')
        
        # Autenticación basada en el email
        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            return JsonResponse({"status": "error", "message": "El correo electrónico no está registrado."})
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"status": "success", "message": "Inicio de sesión exitoso.", "redirect": "index"})
        else:
            return JsonResponse({"status": "error", "message": "Correo electrónico o contraseña incorrectos."})

    return render(request, 'cuenta.html')

def listaProductos(request):
    productos = Producto.objects.all()
    return render(request, 'html/listaProductos.html', {'productos': productos})

def agregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listaProductos')  # Redirigir a la lista de productos después de agregar
    else:
        form = ProductoForm()
    return render(request, 'html/agregarProducto.html', {'form': form})