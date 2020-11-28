from django.db import models

# Create your models here.
class NaveNodriza(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=50)