from django.urls import path
from .views import *

urlpatterns = [
    path('crear_aula/', crear_aula),
    path("listar_aulas/", listar_aulas),
    path('tutores/', tutores, name="tutores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('aulas/', aulas, name="aulas"),
    path('desafios/', desafios, name="desafios"),
    path('busquedaComision/', busquedaComision, name="busquedaComision"),
    path('buscar/', buscar, name="buscar"),
]

