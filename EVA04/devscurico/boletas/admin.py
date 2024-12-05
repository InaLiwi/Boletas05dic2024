from django.contrib import admin
from .models import *

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ('nombre', 'email')

@admin.register(Boleta)
class boletaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'estado', 'prioridad', 'tecnico_asignado', 'fecha_creacion')
    list_filter = ('estado', 'prioridad', 'tecnico_asignado')
    search_fields = ('cliente__nombre', 'descripcion')
    date_hierarchy = 'fecha_creacion'





# Register your models here.
