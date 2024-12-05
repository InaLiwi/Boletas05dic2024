from django import forms
from .models import *

class BoletaForm(forms.ModelForm):
    class Meta:
        model = breakpointoleta
        fields = ['cliente', 'descripcion', 'prioridad', 'estado', 'tecnico_asignado']


