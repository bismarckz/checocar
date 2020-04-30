from django.contrib import admin
from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [

path(
        '',
        views.HomePage.as_view(),
        name='panel0',
    ),

path(
        'home/',
        views.HomePage.as_view(),
        name='panel',
    ),

path(
        'confirmar_viaje/',
        views.SampleView.as_view(), # PruebaCreateView- MyCreateView -  SampleView
        name='userviajes',
    ),
]
