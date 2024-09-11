from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    CATEGORIAS = [
        ('alta', 'Gama Alta'),
        ('media', 'Gama Media'),
        ('baja', 'Gama Baja'),
        ('otros', 'Otros'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=10, choices=CATEGORIAS, default='otros')
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class HistorialCompra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.producto.nombre} - {self.fecha_compra}'