from django import forms
from apps.pasajero.models import Pasajero

class PasajeroForm(forms.ModelForm):

    class Meta:
        model = Pasajero

        fields = [
            'id',
            'nombre',
        ]
        lables = {
            'id': 'Identificador',
            'nombre': 'Nombre',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }