from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.http import HttpResponse
import json
from .forms import ProductoForm, Producto
from django.contrib.auth.decorators import login_required
from .carrito_models import Carrito, ItemCarrito
from django.conf import settings
import paypalrestsdk
from .paypal import paypalrestsdk
import logging
from decimal import Decimal
from django.urls import reverse
import random


from django.shortcuts import render
from .models import Producto
import random

def index(request):
    productos = list(Producto.objects.all())
    productos_destacados = random.sample(productos, min(len(productos), 4))
    productos_oferta = list(Producto.objects.filter(categoria='otros'))
    if len(productos_oferta) > 3:
        productos_oferta = random.sample(productos_oferta, 3)
    
    for producto in productos_destacados + productos_oferta:
        if producto.imagen:
            producto.image_url = producto.imagen.url
        else:
            producto.image_url = 'https://via.placeholder.com/150'
    
    return render(request, 'html/index.html', {
        'productos_destacados': productos_destacados,
        'productos_oferta': productos_oferta,
    })


def acercade(request):
    return render(request, 'html/acercade.html')

def carrocompras(request):
    return render(request, 'html/carrocompras.html')

def cuenta(request):
    return render(request, 'html/cuenta.html')

def gama_alta(request):
    productos = Producto.objects.filter(categoria='alta')
    for producto in productos:
        if producto.imagen:
            producto.image_url = producto.imagen.url
        else:
            producto.image_url = 'https://via.placeholder.com/150'
    return render(request, 'html/GamaAlta.html', {'productos': productos})

def gama_media(request):
    productos = Producto.objects.filter(categoria='media')
    for producto in productos:
        if producto.imagen:
            producto.image_url = producto.imagen.url
        else:
            producto.image_url = 'https://via.placeholder.com/150'
    return render(request, 'html/GamaMedia.html', {'productos': productos})


def gama_baja(request):
    productos = Producto.objects.filter(categoria='baja')
    for producto in productos:
        if producto.imagen:
            producto.image_url = producto.imagen.url
        else:
            producto.image_url = 'https://via.placeholder.com/150'
    return render(request, 'html/GamaBaja.html', {'productos': productos})

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

@login_required
def agregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agregarProducto')  # Redirigir a la misma página después de agregar
    else:
        form = ProductoForm()
    productos = Producto.objects.all()
    return render(request, 'html/agregarProducto.html', {'form': form, 'productos': productos})

@login_required
def modificarProducto(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        nuevo_precio = request.POST.get('precio')
        producto = get_object_or_404(Producto, id=producto_id)
        producto.precio = nuevo_precio
        producto.save()
        return redirect('agregarProducto')

@login_required
def eliminarProducto(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        producto = get_object_or_404(Producto, id=producto_id)
        producto.delete()
        return redirect('agregarProducto')
    
    





@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    total = sum(item.total() for item in carrito.items.all())
    return render(request, 'html/ver_carrito.html', {'carrito': carrito, 'total': total})

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('ver_carrito')


#paypal api
@login_required
def procesar_pago(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    total_clp = sum(item.total() for item in carrito.items.all())
    
    # Convertir total_clp a float
    total_clp_float = float(total_clp)
    
    # Tasa de conversión CLP a USD actualizada
    conversion_rate = 0.0011  # Tasa de conversión correcta
    total_usd = total_clp_float * conversion_rate
    
    pago = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "transactions": [{
            "amount": {
                "total": f"{total_usd:.2f}",
                "currency": "USD"},
            "description": "Compra en CoreTech"}],
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('paypal_return')),
            "cancel_url": request.build_absolute_uri(reverse('paypal_cancel'))}})

    if pago.create():
        for link in pago.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    else:
        logging.error(pago.error)
        return HttpResponse("Error al crear el pago en PayPal")


@login_required
def paypal_return(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        carrito = Carrito.objects.get(usuario=request.user)
        carrito.items.all().delete()  # Vaciar el carrito
        return render(request, 'html/success.html')
    else:
        return render(request, 'html/error.html', {'error': payment.error})

@login_required
def paypal_cancel(request):
    return render(request, 'html/cancel.html')


