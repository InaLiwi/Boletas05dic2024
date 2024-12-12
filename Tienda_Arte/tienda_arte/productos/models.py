from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    def actualizar_stock(self, cantidad):
        if self.stock - cantidad < 0:
            raise ValidationError("No hay suficiente stock disponible.")
        self.stock -= cantidad
        self.save()

class Trabajador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=Trabajador)
def add_user_to_trabajadores_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Trabajadores')
        instance.user.groups.add(group)

