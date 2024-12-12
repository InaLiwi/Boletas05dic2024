"""
URL configuration for tienda_arte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from productos import views as productos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', productos_views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', productos_views.detalle_producto, name='detalle_producto'),
    path('agregar-al-carrito/<int:producto_id>/', productos_views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', productos_views.carrito, name='carrito'),
    path('ajustar-cantidad-carrito/<int:detalle_id>/', productos_views.ajustar_cantidad_carrito, name='ajustar_cantidad_carrito'),
    path('completar-orden/', productos_views.completar_orden, name='completar_orden'),
    path('panel-trabajador/', productos_views.panel_trabajador, name='panel_trabajador'),
    path('editar-producto/<int:producto_id>/', productos_views.editar_producto, name='editar_producto'),
    path('agregar-producto/', productos_views.agregar_producto, name='agregar_producto'),
    path('eliminar-producto/<int:producto_id>/', productos_views.eliminar_producto, name='eliminar_producto'),
    path('informe-ventas/', productos_views.informe_ventas, name='informe_ventas'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


