from django import forms

class NewUserViajeForms(forms.Form):

    viaje = forms.CharField(max_length=20)
    user = forms.CharField(max_length=20) #, unique=True
    cantidad = forms.CharField(max_length=20)
#ForeignKey(User, on_delete=models.CASCADE)
