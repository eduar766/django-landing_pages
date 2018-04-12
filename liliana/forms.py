from django import forms
from .models import MensajeLiliana

class MensajeLilianaForm(forms.ModelForm):
    class Meta:
        model = MensajeLiliana
        fields = ['name', 'email', 'telefono']
        widgets = {
            'name': forms.TextInput(
                attrs={}
            ),
            'email': forms.TextInput(
                attrs={}
            ),
            'telefono': forms.TextInput(
                attrs={}
            )
        }
