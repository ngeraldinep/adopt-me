from django.contrib import admin
from .models import Project, Task, Persona, TipoCursada, Datos_Personales, Cursos, Confirmados,Lazarillo, Fechas, ConsultaReclamo, Adoptar, Colegio, Animal

# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
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