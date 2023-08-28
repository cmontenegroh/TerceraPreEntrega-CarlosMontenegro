from django.contrib import admin
from .models import Aula, Estudiante, Tutor, Desafio
# Register your models here.

admin.site.register(Aula)
admin.site.register(Estudiante)
admin.site.register(Tutor)
admin.site.register(Desafio)