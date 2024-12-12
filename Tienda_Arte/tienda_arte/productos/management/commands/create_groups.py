from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from productos.models import Producto

class Command(BaseCommand):
    help = 'Crea grupos de usuarios y asigna permisos'

    def handle(self, *args, **options):
        # Crear grupo de Clientes
        cliente_group, created = Group.objects.get_or_create(name='Clientes')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo de Clientes creado exitosamente'))
        else:
            self.stdout.write(self.style.WARNING('El grupo de Clientes ya existe'))

        # Crear grupo de Trabajadores
        trabajador_group, created = Group.objects.get_or_create(name='Trabajadores')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo de Trabajadores creado exitosamente'))
        else:
            self.stdout.write(self.style.WARNING('El grupo de Trabajadores ya existe'))

        # Obtener permisos para el modelo Producto
        content_type = ContentType.objects.get_for_model(Producto)
        producto_permissions = Permission.objects.filter(content_type=content_type)

        # Asignar permisos al grupo de Trabajadores
        for perm in producto_permissions:
            trabajador_group.permissions.add(perm)
        
        self.stdout.write(self.style.SUCCESS('Permisos asignados al grupo de Trabajadores'))

        # Asignar permisos de los clientes
        self.stdout.write(self.style.SUCCESS('Grupos y permisos configurados exitosamente'))

# python manage.py create_groups --> para crear los grupos en admin