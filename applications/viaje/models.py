from django.db import models
# apps tercero
from PIL import Image

from . managers import ViajeManager
# Create your models here.
class Viaje(models.Model):
    """ Modelo para tabla viaje """

    origen = models.CharField('Origen', max_length=60)
    destino = models.CharField('Destino', max_length=60)
    fecha = models.DateField('Fecha',blank=False, null=False,)

    horario = models.TimeField('Horario',auto_now=False, auto_now_add=False)
    mapa =  models.URLField('Mapa', max_length=500)
    lugares = models.PositiveIntegerField(default=0)

    objects= ViajeManager()

    def __str__(self):
        return str(self.id)
