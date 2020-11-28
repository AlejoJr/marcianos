from django.db import models
from django.core.validators import RegexValidator
from apps.navenodriza.models import NaveNodriza

# Create your models here.
class Aeronave(models.Model):
    id = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    nombre = models.CharField(max_length=50)
    max_marcianos = models.IntegerField()
    origen = models.ForeignKey(NaveNodriza,related_name='origennavenodriza', null=True, blank=True, on_delete=models.CASCADE)
    destino = models.ForeignKey(NaveNodriza,related_name='destinonavenodriza',null=True, blank=True, on_delete=models.CASCADE)