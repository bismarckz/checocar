from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)


from django.views.generic.edit import (
    FormView
)
# models
from .models import Viaje
from .forms import NewUserViajeForms
# forms
#from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'inicio.html'

class ViajesView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'viaje.html'


class ViajesDetailView(DetailView):
    model = Viaje
    template_name = "viaje/detail_viaje.html"

    def get_context_data(self, **kwargs):
        context = super(ViajesDetailView, self).get_context_data(**kwargs)
        #toot un proceso
        context['origen'] = 'Viaje del mes'
        return context


class ListAllViajes(ListView):
    template_name = 'viaje/list_all.html'
    context_object_name = 'viaje'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        f1 = self.request.GET.get("fecha1", '')
        f2 = self.request.GET.get("fecha2", '')

        if f1 and f2:
            return Viaje.objects.listar_viajes2(palabra_clave, f1, f2)
        else:
            return Viaje.objects.listar_viajes(palabra_clave)



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
