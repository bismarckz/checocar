from django.db import models
from applications.viaje.models import Viaje
from applications.users.models import User


class UserViaje(models.Model): #collection name
    #cuando fue insertado y actualizado
    apartartado = models.DateTimeField(auto_now_add=True, auto_now=False)
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #, unique=True
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return  str(self.viaje.id) + str(self.user.id)
