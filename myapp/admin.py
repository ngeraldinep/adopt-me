from django.contrib import admin
from .models import Project, Task, Cursos, TipoConsultaReclamo, FormularioConsultas

# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Cursos)
admin.site.register(TipoConsultaReclamo)
admin.site.register(FormularioConsultas)


