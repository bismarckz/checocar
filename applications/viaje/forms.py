from django import forms

class NewUserViajeForms(forms.Form):


    user = forms.IntegerField() #, unique=True
    cantidad = forms.IntegerField()
#ForeignKey(User, on_delete=models.CASCADE)

    viaje = forms.IntegerField(
        label='Contraseña',
        required=True,

    )


def clean_viaje(self):
    #recuperamos la variable
    viaje = self.cleaned_data['id_viaje']

    return viaje
