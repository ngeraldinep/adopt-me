from django.db import models
# Con on_delete le decimos que tiene q hacer cuando se borrra un projecto
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    
class Task(models.Model):
    title =  models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title + ' - ' + self.project.name
    

class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_curso

class TipoConsultaReclamo(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class FormularioConsultas(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=8)
    correo = models.EmailField()
    #tipo_consulta_reclamo = models.ForeignKey(TipoConsultaReclamo, on_delete=models.CASCADE)
    texto_libre = models.TextField()
    #checkbox_llamado = models.BooleanField(default=False)

    def __str__(self):
        return self.correo + ' - ' + self.tipo_consulta_reclamo.nombre

    
# class Datos_persona(models.Model):
#     nombre =  models.CharField(max_length=30)
#     apellido =  models.CharField(max_length=30)
#     correo =  models.CharField(max_length=60)
#     telefono =  models.IntegerField(max_length=8)
#     dni =  models.IntegerField(max_length=8)
#     fecha_nacimiento = models.DateField()



# class Datos_geograficos(models.Model):
#     barrio =  models.CharField(max_length=30)
#     provincia =  models.CharField(max_length=30)
#     pais =  models.CharField(max_length=30)



#     msj = models.TextField()


# class Datos_ocupacio(models.Model):    
#     ocupacion = models.TextField()
    
#     curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    
#     adoptar = models.TextField()
    



    
#     def __str__(self):
#         return self.title + ' - ' + self.project.name
    
# class Formulario_adopcion(models.Model):
#     title =  models.CharField(max_length=200)
#     description = models.TextField()
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     done = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.title + ' - ' + self.project.name