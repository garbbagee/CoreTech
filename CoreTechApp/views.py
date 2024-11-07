from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.http import HttpResponse
import json
from .forms import ProductoForm, Producto, UsernameChangeForm  
from django.contrib.auth.decorators import login_required
from .carrito_models import Carrito, ItemCarrito
from django.conf import settings
import paypalrestsdk
from .paypal import paypalrestsdk
import logging
from decimal import Decimal
from django.urls import reverse
from django.utils import timezone
import random
from django.shortcuts import render
from .models import Producto
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from decimal import Decimal
from .models import HistorialCompra
from django.http import JsonResponse
from .models import Producto
from django.views.decorators.csrf import csrf_exempt



def buscar_productos(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre__icontains=query)
    productos_data = list(productos.values('id', 'nombre', 'descripcion', 'precio', 'imagen'))  # Solo los campos necesarios
    return JsonResponse({'productos': productos_data})










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

def user_logout(request):
    logout(request)
    return redirect('index')  # Cambia 'index' por el nombre de la URL a la que quieres redirigir al usuario después del logout



def perfil(request):
    historial_compras = HistorialCompra.objects.filter(usuario=request.user)
    return render(request, 'html/perfil.html', {'user': request.user, 'historial_compras': historial_compras})


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
def agregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agregarProducto')
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

@login_required
def procesar_pago(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    total_clp = sum(item.total() for item in carrito.items.all())
    
    total_clp_float = float(total_clp)
    conversion_rate = 0.0011
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
                logging.info(f"Redirigiendo a PayPal: {link.href}")
                return redirect(link.href)
    else:
        logging.error(pago.error)
        return HttpResponse("Error al crear el pago en PayPal")

from django.utils import timezone

@login_required
def paypal_return(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        carrito = Carrito.objects.get(usuario=request.user)
        items = list(carrito.items.all())  # Guardamos los items antes de vaciar el carrito
        total = sum(float(item.total()) for item in items)  # Convertir a float

        # Guardar los items y el total en la sesión antes de vaciar el carrito
        request.session['boleta_items'] = [{'producto': item.producto.nombre, 'cantidad': item.cantidad, 'precio': float(item.producto.precio)} for item in items]
        request.session['boleta_total'] = float(total)

        # Guardar los productos comprados en el historial de compras del usuario
        for item in items:
            HistorialCompra.objects.create(
                usuario=request.user,
                producto=item.producto,
                fecha_compra=timezone.now()
            )

        # Limpiar el carrito después de guardar el historial
        carrito.items.all().delete()

        return redirect('thank_you')
    else:
        return render(request, 'html/error.html', {'error': payment.error})




@login_required
def paypal_cancel(request):
    return render(request, 'html/cancel.html')

@login_required
def thank_you(request):
    return render(request, 'html/thank_you.html')

@login_required
def descargar_boleta(request):
    # Obtenemos los items y el total desde la sesión
    items_data = request.session.get('boleta_items', [])
    total = request.session.get('boleta_total', 0)

    # Depuración: Verificar que estamos obteniendo los items
    print("Datos de items solicitados para la boleta:", items_data)

    if not items_data:
        print("No se encontraron items para la boleta.")

    # Crear la respuesta PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="boleta.pdf"'
    
    # Generar el contenido de la boleta PDF
    generar_boleta_pdf(response, request.user, items_data, total)
    
    return response


def generar_boleta_pdf(response, usuario, items_data, total):
    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica", 12)
    
    # Encabezado
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, "Boleta de Compra")
    
    # Información del comprador
    p.setFont("Helvetica", 12)
    p.drawString(100, 730, f"Comprador: {usuario.username}")
    p.drawString(100, 710, f"Email: {usuario.email}")
    
    # Detalles de la compra
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, 680, "Detalles de la Compra:")

    y_position = 660
    p.setFont("Helvetica", 12)
    for item_data in items_data:
        p.drawString(100, y_position, f"Producto: {item_data['producto']} - Cantidad: {item_data['cantidad']} - Precio: ${item_data['precio']:.2f} CLP")
        y_position -= 20
    
    # Total de la compra
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y_position - 20, f"Total: ${total:.2f} CLP")
    
    p.showPage()
    p.save()


    

@login_required
def perfil(request):
    historial_compras = HistorialCompra.objects.filter(usuario=request.user)
    
    if request.method == 'POST':
        form = UsernameChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'¡Nombre de usuario actualizado con éxito a {request.user.username}!')
            return redirect('perfil')
        else:
            messages.error(request, 'Hubo un error al actualizar el nombre de usuario. Por favor, intenta nuevamente.')
    else:
        form = UsernameChangeForm(instance=request.user)
    
    return render(request, 'html/perfil.html', {
        'user': request.user,
        'historial_compras': historial_compras,
        'form': form,
    })

@login_required
def borrar_compra_individual(request, compra_id):
    compra = get_object_or_404(HistorialCompra, id=compra_id, usuario=request.user)
    compra.delete()
    messages.success(request, 'Compra eliminada con éxito.')
    return redirect('perfil')

def borrar_historial(request):
    HistorialCompra.objects.filter(usuario=request.user).delete()
    messages.success(request, 'Historial de compras eliminado con éxito.')
    return redirect('perfil')

@csrf_exempt  # Permite el uso de la autenticación CSRF para solicitudes AJAX
def eliminar_usuario(request):
    if request.method == 'POST':
        # Parsear los datos JSON enviados
        data = json.loads(request.body.decode('utf-8'))
        password = data.get('password', '')

        # Verificar que el usuario no sea el administrador
        if request.user.email == "admin@gmail.com":
            return JsonResponse({'success': False, 'error': 'No puedes eliminar al administrador.'})

        # Autenticar al usuario con la contraseña proporcionada
        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            # Si la autenticación es exitosa, eliminar al usuario y cerrar sesión
            request.user.delete()
            logout(request)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Contraseña incorrecta.'})
    
    return JsonResponse({'success': False, 'error': 'Método no permitido.'})