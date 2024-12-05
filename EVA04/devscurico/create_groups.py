import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devscurico.settings")
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from boletas.models import *

def create_groups():
    # Crear grupo de Técnicos
    tecnicos_group, created = Group.objects.get_or_create(name='Técnicos')
    
    # Permisos para Técnicos
    boleta_content_type = ContentType.objects.get_for_model(Boleta)
    
    tecnicos_permissions = [
        Permission.objects.get(content_type=boleta_content_type, codename='view_boleta'),
        Permission.objects.get(content_type=boleta_content_type, codename='change_boleta'),
    ]
    
    tecnicos_group.permissions.set(tecnicos_permissions)
    
    # Crear grupo de Administradores
    admin_group, created = Group.objects.get_or_create(name='Administradores')
    
    # Permisos para Administradores (todos los permisos)
    admin_permissions = Permission.objects.all()
    admin_group.permissions.set(admin_permissions)
    
    print("Grupos y permisos creados exitosamente.")

if __name__ == '__main__':
    create_groups()

