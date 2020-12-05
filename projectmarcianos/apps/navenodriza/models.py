from django.db import models

# Create your models here.
class NaveNodriza(models.Model):
    identificador = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)