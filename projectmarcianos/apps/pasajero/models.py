from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Pasajero(models.Model):
    id = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    nombre = models.CharField(max_length=30)