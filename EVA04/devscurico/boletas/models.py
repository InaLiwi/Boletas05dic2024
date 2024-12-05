from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre



class Producto:
    id_producto = models.AutoField()
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Descripción: {self.descripcion} | Precio: ${self.precio} | Categoria: {self.categoria} | Stock: {self.stock}"
    

class Boleta:
    id_boleta = models.AutoField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID Boleta: {self.id_boleta} | Cliente: {self.cliente}"

class BoletaProducto :
    id_boleta = models.ForeignKey('Boleta', on_delete=models.CASCADE)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField(max_length=3)

    def __str__(self):
        return f"ID Boleta: {self.id_boleta} | ID Producto: {self.id_producto} | Cantidad: {self.cantidad}"