from django.contrib import admin
from .models import Persona, Datos_Personales, TipoCursada, Cursos, Turno, Confirmados, Lazarillo, Fechas, Animal, Adoptar, ConsultaReclamo, Colegio

# Register your models here.

admin.site.register(Persona)
admin.site.register(Datos_Personales)
admin.site.register(ConsultaReclamo)
admin.site.register(TipoCursada)
admin.site.register(Cursos)
admin.site.register(Confirmados)
admin.site.register(Fechas)
admin.site.register(Lazarillo)
admin.site.register(Adoptar)
admin.site.register(Colegio)
admin.site.register(Animal)
admin.site.register(Turno)