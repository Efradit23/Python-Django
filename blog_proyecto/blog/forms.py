from django import forms
from .models import Publicacion

class PublicacionFormulario(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'autor']