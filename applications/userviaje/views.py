from django.shortcuts import render
from django.views.generic.edit import FormView
# Create your views here.

from . forms import NewUserViajeForms

#from . models import UserViaje
from applications.viaje.models import Viaje
from applications.users.models import User
from .models import UserViaje
from .forms import NewUserViajeForms

#from django import forms

class NewRegisterUserViajeView(FormView):
    template_name = 'viaje/detail_viaje.html'
    form_class = NewUserViajeForms
    success_url = '/viajes'


    #ocupanos sobreescribir la funcion
    def form_valid(self, form):
        print("Estamos en el formvies")

        viaje = form.cleaned_data['id_viaje']
        curso = form.cleaned_data['id_curso']
        cantidad = form.cleaned_data['pasajeros']


        UserViaje.objects.create(
        apartartado = apartartado,
        viaje = Travel,
        cantidad = cantidad,

        )

        return super(NewRegisterUserViajeView.self).form_valid(form)
