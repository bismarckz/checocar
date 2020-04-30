from django.contrib import admin
from django.urls import path

from . import views

app_name = "viajes_app"

urlpatterns = [

path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),

path(
        'viajes/',
        views.ListAllViajes.as_view(),
        name='viajes_all'
    ),

path(
        'viajes/<pk>/',
        views.ViajesDetailView.as_view(),
        name='viaje_detail'
    ),

path(
        'viaje_apartado/',
        views.NewRegisterUserViajeView.as_view(),
        name='viaje_detail'
    ),

]
