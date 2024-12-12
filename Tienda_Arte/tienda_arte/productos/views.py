from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Producto, Trabajador
from .forms import ProductoForm
from ordenes.models import Orden, DetalleOrden
import django.db.models as models

def es_trabajador(user):
    return user.groups.filter(name='Trabajadores').exists()

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    orden, creada = Orden.objects.get_or_create(usuario=request.user, completada=False)
    detalle_orden, creado = DetalleOrden.objects.get_or_create(orden=orden, producto=producto)
    
    if not creado:
        detalle_orden.cantidad += 1
        detalle_orden.save()

    return redirect('carrito')

@login_required
def carrito(request):
    orden, creada = Orden.objects.get_or_create(usuario=request.user, completada=False)
    return render(request, 'productos/carrito.html', {'orden': orden})

@login_required
def completar_orden(request):
    orden = get_object_or_404(Orden, usuario=request.user, completada=False)
    try:
        with transaction.atomic():
            for detalle in orden.detalleorden_set.all():
                detalle.producto.actualizar_stock(detalle.cantidad)
            orden.completada = True
            orden.save()
        messages.success(request, "Tu orden ha sido completada exitosamente.")
        return render(request, 'productos/boleta.html', {'orden': orden})
    except ValidationError as e:
        messages.error(request, str(e))
        return redirect('carrito')

@user_passes_test(es_trabajador)
def panel_trabajador(request):
    productos = Producto.objects.all()
    return render(request, 'productos/panel_trabajador.html', {'productos': productos})

@user_passes_test(es_trabajador)
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado exitosamente.')
            return redirect('panel_trabajador')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

@user_passes_test(es_trabajador)
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('panel_trabajador')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto})

@user_passes_test(es_trabajador)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.delete()
    return redirect('panel_trabajador')

@user_passes_test(es_trabajador)
def informe_ventas(request):
    ordenes = Orden.objects.filter(completada=True)
    total_ventas = sum(orden.total() for orden in ordenes)
    productos_vendidos = DetalleOrden.objects.filter(orden__completada=True).values('producto__nombre').annotate(total=models.Sum('cantidad')).order_by('-total')
    return render(request, 'productos/informe_ventas.html', {
        'ordenes': ordenes,
        'total_ventas': total_ventas,
        'productos_vendidos': productos_vendidos
    })

@login_required
def ajustar_cantidad_carrito(request, detalle_id):
    detalle = get_object_or_404(DetalleOrden, id=detalle_id, orden__usuario=request.user, orden__completada=False)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 0))
        if cantidad > 0:
            detalle.cantidad = cantidad
            detalle.save()
        else:
            detalle.delete()
    return redirect('carrito')
