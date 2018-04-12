from django import forms
from .models import MensajeBailante

class MensajeBailanteForm(forms.ModelForm):
    class Meta:
        model = MensajeBailante
        fields = ['name', 'email', 'telefono']
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'placeholder': 'Nombre y Apellido'
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    'placeholder': 'Correo electrónico'
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'placeholder': 'Teléfono'
                }
            )
        }
