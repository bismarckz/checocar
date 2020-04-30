from django.contrib import admin
from django.urls import path

from . import views

app_name = "cursos_app"

urlpatterns = [

path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),

path(
        'cursos/',
        views.ListAllCursos.as_view(),
        name='cursos_all'
    ),

path(
        'cursos/<pk>/',
        views.CursosDetailView.as_view(),
        name='curso_detail'
    ),


]
