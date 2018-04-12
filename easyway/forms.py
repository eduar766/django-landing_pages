from django import forms
from .models import EnviarMensaje, EnviarMensajeTwo

class EnviarMensajeForm(forms.ModelForm):
    class Meta:
        model = EnviarMensajeTwo
        fields = ['name', 'email', 'empresa', 'telefono', 'hora']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder' : 'Nombre y Apellido'}),
            'email': forms.TextInput(
                attrs={'placeholder' : 'Correo Electrónico'}),
            'empresa': forms.TextInput(
                attrs={'placeholder' : 'Empresa'}),
            'telefono': forms.TextInput(
                attrs={'placeholder' : 'Teléfono'}),
            'hora': forms.TextInput(
                attrs={'placeholder' : '¿Cuando te contactamos?'}),
        }
