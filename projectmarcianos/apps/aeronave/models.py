from django.db import models
from django.core.validators import RegexValidator
from apps.navenodriza.models import NaveNodriza
from apps.pasajero.models import Pasajero
import datetime
# Create your models here.
class Aeronave(models.Model):
    id = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    nombre = models.CharField(max_length=50)
    max_marcianos = models.IntegerField()
    origen = models.ForeignKey(NaveNodriza,related_name='origennavenodriza', null=True, blank=True, on_delete=models.CASCADE)
    destino = models.ForeignKey(NaveNodriza,related_name='destinonavenodriza',null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)

class GestionPasajeros(models.Model):
    BOOL_CHOICES = ((True, 'Asignar pasajero'), (False, 'Bajar pasajero'))
    pasajero = models.ForeignKey(Pasajero, null=True, blank=True, on_delete=models.CASCADE)
    aeronave = models.ForeignKey(Aeronave, null=True, blank=True, on_delete=models.CASCADE)
    activo = models.BooleanField(choices=BOOL_CHOICES)


class RegistroNaveRevisada(models.Model):
    aeronave = models.ForeignKey(Aeronave, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField()

class ListadoRevisionNave(models.Model):
    identificador = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField(default=datetime.date.today)
    gestionpasajeros = models.ForeignKey(GestionPasajeros, null=True, blank=True, on_delete=models.CASCADE)

class HistorialNaveRevisada(models.Model):
    aeronave = models.ForeignKey(Aeronave, null=True, blank=True, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    identificador = models.CharField(max_length=10)