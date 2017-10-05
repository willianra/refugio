
from django.db import models



# Create your models here.
# from django.db.models.fields.related import ForeignKey
from django.db.models import ForeignKey

from adopcion.models import Persona


class Vacuna (models.Model):
    nombre =models.CharField(max_length=50)

class Mascota(models.Model):
    nombre=models.CharField(max_length=50)
    sexo =models.CharField(max_length=10)
    edad_aproximada =models.IntegerField()
    fecha_rescate = models.DateField()
    cod_persona = ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
    vacuna =models.ManyToManyField(Vacuna)
