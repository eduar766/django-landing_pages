from django import forms
from .models import RecicladoraMensaje, Galeria

class RecicladoraMensajeForms(forms.ModelForm):
    class Meta:
        model = RecicladoraMensaje
        fields = ['name', 'email', 'telefono', 'mensaje']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Nombre'}
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email'}
            ),
            'telefono': forms.TextInput(
                attrs={'placeholder': 'Teléfono'}
            ),
            'mensaje': forms.Textarea(
                attrs={'placeholder': 'Mensaje'}
            )
        }

class GaleriaForms(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ['name', 'model_pic']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Nombre'}
            ),
            'model_pic': forms.ImageField(
                
            ),
        }
