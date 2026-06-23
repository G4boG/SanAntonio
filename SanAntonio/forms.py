from django import forms
from .models import Escolar

# Creamos un formulario que copia la estructura de nuestro modelo
class EscolarForm(forms.ModelForm):
    class Meta:
        model = Escolar
        # Le decimos a Django qué campos queremos que el usuario pueda rellenar en la web
        fields = ['nombre', 'categoria', 'stock', 'ubicacion']