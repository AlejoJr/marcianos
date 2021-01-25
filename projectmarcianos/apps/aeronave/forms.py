from django import forms
from apps.aeronave.models import Aeronave, GestionPasajeros, RegistroNaveRevisada, ListadoRevisionNave

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

class GestionarPasajeroForm(forms.ModelForm):
    class Meta:
        model = GestionPasajeros

        fields = [
            'pasajero',
            'aeronave',
            'activo',
        ]
        lables = {
            'pasajero': 'Pasajero',
            'aeronave': 'Aeronave',
            'activo': 'Accion',
        }
        widgets = {
            'pasajero': forms.Select(),
            'aeronave': forms.Select(),
            'activo': forms.Select(),
        }

class RegistroNaveRevisada(forms.ModelForm):
    class Meta:
        model = RegistroNaveRevisada

        fields = [
            'aeronave',
            'fecha',
        ]
        lables = {
            'aeronave': 'Aeronave',
            'fecha': 'Fecha',
        }
        widgets = {
            'aeronave': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(format='%d/%m/%Y'),
        }

class ListadoRevisionNaveForm(forms.ModelForm):
    class Meta:
        model = ListadoRevisionNave

        fields = [
            'identificador',
            'nombre',
            'fecha',
            'gestionpasajeros',
        ]
        lables = {
            'identificador': 'Codigo Revision',
            'nombre': 'Nombre revisor',
            'fecha': 'Fecha',
        }
        widgets = {
            'identificador': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(format='%d/%m/%Y'),
        }