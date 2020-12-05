from django import forms
from apps.aeronave.models import Aeronave

class AeronaveForm(forms.ModelForm):

    class Meta:
        model = Aeronave

        fields = [
            'id',
            'nombre',
            'max_marcianos',
            'origen',
            'destino',
        ]
        lables = {
            'id': 'Identificador',
            'nombre': 'Nombre',
            'max_marcianos': 'Cupo de Nave',
            'origen': 'Origen',
            'destino': 'Destino',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'max_marcianos': forms.TextInput(attrs={'class': 'form-control'}),
            'origen': forms.Select(),
            'destino': forms.Select(),
        }