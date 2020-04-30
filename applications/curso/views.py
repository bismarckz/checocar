from django.shortcuts import render

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
# models
from .models import Curso
# forms
#from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'inicio.html'

class CursosView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'curso.html'


class CursosDetailView(DetailView):
    model = Curso
    template_name = "curso/detail_curso.html"

    def get_context_data(self, **kwargs):
        context = super(CursosDetailView, self).get_context_data(**kwargs)
        #toot un proceso
        context['nombre'] = 'Curso del mes'
        return context


class ListAllCursos(ListView):
    template_name = 'curso/list_all.html'
    context_object_name = 'curso'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        f1 = self.request.GET.get("fecha1", '')
        f2 = self.request.GET.get("fecha2", '')

        if f1 and f2:
            return Curso.objects.listar_cursos2(palabra_clave, f1, f2)
        else:
            return Curso.objects.listar_cursos(palabra_clave)
