from django.db import models

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