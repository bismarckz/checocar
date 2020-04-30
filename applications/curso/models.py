from django.db import models
# apps tercero
from PIL import Image

from . managers import CursoManager
# Create your models here.
class Curso(models.Model):
    """ Modelo para tabla curso """

    nombre = models.CharField('Nombre', max_length=60)
    direccion = models.CharField('Destino', max_length=60)
    fecha = models.DateField('Fecha',blank=False, null=False,)

    horario = models.TimeField('Horario',auto_now=False, auto_now_add=False)
    mapa =  models.URLField('Mapa', max_length=500)
    

    objects= CursoManager()

    def __str__(self):
        return str(self.id)
