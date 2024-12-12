from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f'Orden {self.id} de {self.usuario.username}'

    def total(self):
        return sum(detalle.subtotal() for detalle in self.detalleorden_set.all())

class DetalleOrden(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad
