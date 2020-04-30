import datetime

from django.db import models

from django.db.models import Q


class CursoManager(models.Manager):
    """ managers para el modelo autor """

    def listar_cursos(self, kword):

        resultado = self.filter(
            Q(nombre__icontains=kword),

        )

        return resultado



    def listar_viajes2(self, kword, fecha1, fecha2):

        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        resultado = self.filter(
            Q(origen__icontains=kword) | Q(destino__icontains=kword),
            fecha__range=(date1,date2)
        )

        return resultado
