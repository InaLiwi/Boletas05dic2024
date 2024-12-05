from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('boletas/', views.lista_boleta, name='lista_boleta'),
    path('boleta/<int:boleta_id>/', views.detalle_boleta, name='detalle_boleta'),
    path('crear/', views.crear_productos, name='crear_productos'),
    path('actualizar/<int:boleta_id>/', views.actualizar_boleta, name='actualizar_boleta'),
    path('eliminar/<int:boleta_id>/', views.eliminar_boleta, name='eliminar_boleta'),
    path('informes/', views.informes, name='informes'),
]

