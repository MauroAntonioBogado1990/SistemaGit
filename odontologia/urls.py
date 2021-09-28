from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pacientes", views.personas_listar, name="pacientes"),
    path("nuevo_paciente", views.nuevo_paciente, name="nuevo_paciente"),
    path("modificar_persona/<int:pk>",
         views.modificar_paciente, name="modificar_paciente"),
    path("eliminar_persona/<int:pk>",
         views.eliminar_paciente, name="eliminar_paciente")
]
