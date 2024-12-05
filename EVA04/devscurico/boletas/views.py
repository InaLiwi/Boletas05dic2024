from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Avg, Count, F
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from .models import *
from .forms import *

@login_required
def inicio(request):
    return render(request, 'boletas/inicio.html')

@login_required
@permission_required('boletas.view_boleta', raise_exception=True)
def lista_boleta(request):
    boletas = Boleta.objects.all()
    return render(request, 'boletas/listar_boletas.html',{'boletas': boletas})

@login_required
@permission_required('boletas.add_boleta', raise_exception=True)
def crear_productos(request):
    if request.method == 'POST':
        form = BoletaForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('listar_productos')

@login_required
@permission_required('boletas.change_boleta', raise_exception=True)
def actualizar_boleta(request, boleta_id):
   pass

@login_required
@permission_required('boletas.delete_boleta', raise_exception=True)
def eliminar_boleta(request, boleta_id):
    pass





''' ------ NO BORRAR ----- ES NUESTRA FUNCIÓN SECRETA SUPER ESPECIAL
@login_required
@permission_required('boletas.view_boleta', raise_exception=True)
def informes(request):
    # Vista para generar informes, solo accesible por administradores
    if not request.user.groups.filter(name='Administradores').exists():
        raise PermissionDenied
    
    # Cálculo de estadísticas para el informe
    total_boletas = boleta.objects.count()
    boletas_resueltos = boleta.objects.filter(estado='RE').count()
    tiempo_promedio_resolucion = boleta.objects.filter(estado='RE').aggregate(
        avg_time=Avg(F('fecha_resolucion') - F('fecha_creacion'))
    )['avg_time']
    boletas_por_tecnico = boleta.objects.values('tecnico_asignado__username').annotate(
        total=Count('id')
    )

    context = {
        'total_boletas': total_boletas,
        'boletas_resueltos': boletas_resueltos,
        'tiempo_promedio_resolucion': tiempo_promedio_resolucion,
        'boletas_por_tecnico': boletas_por_tecnico,
    }
    return render(request, 'boletas/informes.html', context)

'''