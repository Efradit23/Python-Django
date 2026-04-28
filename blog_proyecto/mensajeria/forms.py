from django import forms
from .models import Mensaje

class MensajeFormulario(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'contenido']
        labels = {
            'destinatario': 'Para',
            'asunto': 'Asunto',
            'contenido': 'Mensaje',
        }