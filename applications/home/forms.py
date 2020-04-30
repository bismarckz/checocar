from django import forms
import requests
from .models import Prueba


class PruebaForm(forms.ModelForm):
    class Meta(object):
        model = Prueba
        fields = (
        'viaje',
        'user',
        'cantidad'
        )

        witgets = {
            'cantidad' :forms.NumberInput(
                attrs = {
                    'initial':'123'
                }
            ),

            'viaje' :forms.ChoiceField(

            )

        }

    def clean_cantidad(self):
        #recuperamos la variable
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero menor a ')
        return cantidad



class NewUserViajeForms(forms.Form):

    user = forms.IntegerField() #initial=2, unique=True
    cantidad = forms.IntegerField()
    viaje = forms.IntegerField()


class MyForm(forms.ModelForm):
    class Meta:
        model=Prueba
        fields=['cantidad']
    #user = forms.IntegerField() #initial=2, unique=True
    #cantidad = forms.IntegerField()
    #viaje = forms.IntegerField()

    def __init__(self, pasajeros=8,*args, **kwargs):
        # we explicit define the foo keyword argument, cause otherwise kwargs will
        # contain it and passes it on to the super class, who fails cause it's not
        # aware of a foo keyword argument.
        super(MyForm, self).__init__(*args, **kwargs)
        print (pasajeros)  # prints the value of the foo url conf param



class PostForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = ('cantidad',)

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




class ContactForm(forms.ModelForm):
    cantidad = forms.IntegerField()

    class Meta:
        model=Prueba
        fields=['user','viaje','cantidad']

    def get_queryset(self):
        print ("creo que si entra")
        if self.request.method == 'GET':
            queryset = Prueba.objects.all()
            state_name = self.request.GET.get('pasajeros', None)
            if state_name is not None:
                queryset = queryset.filter(state__name=state_name)
                print (queryset)
            return queryset



class ContactForms(forms.ModelForm):
    cantidad = forms.IntegerField()

    def __init__(self, pk, *args, **kwargs):
        print("ENTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        self.cantidad = pk
        super(ContactForms, self).__init__(*args, **kwargs)

#    def __init__(self, *args, **kwargs):
#     if kwargs.get('instance'):
#        cantidad = kwargs['instance'].cantidad
#        kwargs.setdefault('initial', {})['cantidad'] = cantidad
#     return super(ContactForm, self).__init__(*args, **kwargs)
