from django import forms
from apps.navenodriza.models import NaveNodriza

class NavenodrizaForm(forms.ModelForm):

    class Meta:
        model = NaveNodriza

        fields = [
            'identificador',
            'nombre',
        ]
        lables = {
            'identificador': 'Identificador',
            'nombre': 'Nombre',
        }
        widgets = {
            'identificador': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }