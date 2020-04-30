import datetime
import requests
from django.shortcuts import render

from django.views.generic.edit import (
    FormView
)
from django.views.generic import (
    CreateView,
    TemplateView,
    ListView,
    DetailView,
)

from .models import Prueba
from .forms import PruebaForm, NewUserViajeForms, PostForm, MyForm, ContactForm



class FechaMixin(object):

    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now()
        return context



class HomePage(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'home/inicio.html'


class ListAllViajesPasajero(ListView):
    template_name = 'home/user_viaje.html'
    context_object_name = 'user_viaje'

    def get_queryset(self):
        #palabra_clave = self.request.GET.get("kword", '')
        #cantidad = self.request.GET.get("cantidad_users", '')

        return Prueba.objects.listar_viajes_user('3')



class SuccessView(TemplateView):
    template_name = 'success.html'



class PruebaCreateView(CreateView):
    template_name = 'userviaje/registerUV.html'
    model = Prueba
    form_class= PostForm
    success_url = '/'

    def my_view(request):

        if request.method == 'POST':
            print (request.POST.get('pasajeros'))

            form = MyForm(request.POST)

            print (form['pasajeros'].value())
            print (form.data['pasajeros'])

            if form.is_valid():
                print (form.cleaned_data['pasajeros'])
                print (form.instance.pasajeros)

                form.save()
                print (form.instance.id)  # now this one can access id/pk



class TestView(FormView):
        template_name = 'userviaje/registerUV.html'
        form_class= NewUserViajeForms
        success_url = '/'

        def home_view(request):
            context ={}

            # dictionary for initial data with
            # field names as keys
            var1 = 1
            var2 = 2
            var3 = 4
            initial_dict = {
                "user" : var1,
                "viaje":var2,
                "cantidad":var3,
            }

            # add the dictionary during initialization
            form = NewUserViajeForms(request.GET, initial = initial_dict)

            context['form']= form
            return render(request, "/", context)



class MyCreateView(CreateView):
    form_class = MyForm
    model = Prueba
    template_name='userviaje/registerUV.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super( MyCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        print (kwargs)
        return kwargs


class CreateContact(CreateView):
    model=Prueba
    template_name='userviaje/registerUV.html'
    form_class=ContactForm




class SampleView(CreateView):
    model=Prueba
    template_name='userviaje/registerUV.html'
    form_class=ContactForm
    success_url = '/'
#    def get_context_data(self, **kwargs):
#        cantidad = Prueba.objects.get(id=kwargs['pasajeros'])
    #def get_context_data(self, **kwargs):
    #    cantidad = Prueba.objects.get(id=kwargs['pasajeros'])
    def profile_page(request):
        print(request.GET)
        #pasajeros = request.GET.get('pasajeros')
        pasajeros = self.request.form['pasajeros']
        print(pasajeros)


    def get_request_example(request):
        # print complete QueryDict
        print(request.GET)
        # print one value of param1
        print(request.GET.get('pasajeros'))
