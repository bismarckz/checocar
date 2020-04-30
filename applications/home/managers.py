import datetime

from django.db import models

from django.db.models import Q


class ViajeUser(models.Manager):
    """ managers para el modelo autor """

    def listar_viajes_user(self, viaje ):
        return self.filter(
            user__id=viaje
        ).order_by('origen')
