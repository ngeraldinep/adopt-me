from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
# Con on_delete le decimos que tiene q hacer cuando se borrra un projecto
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
  
class Task(models.Model):
    title =  models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title + ' - ' + self.project.name
    
class Persona(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre =  models.CharField(max_length=30)
    apellido =  models.CharField(max_length=30)
    telefono =  models.IntegerField()
    correo =  models.CharField(max_length=100)

    def __str__(self):
        return "{}- {}  {}".format(str(self.id), self.apellido, self.nombre )
    
class Datos_Personales(models.Model):    
    id = models.AutoField(primary_key=True)
    dni =  models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} {} - {}".format(self.id_persona.apellido, self.id_persona.nombre, str(self.dni))

class Lazarillo(models.Model):    
    id = models.AutoField(primary_key=True)
    info_adicional = models.TextField(blank=True)
    discapacidad =  models.CharField(max_length=30)
    primer_lazarillo = models.BooleanField(default=False)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} - {} - {}".format(
            self.fecha.strftime('%Y-%m-%d %H:%M:%S'), 
            self.id_persona.nombre, 
            self.id_persona.apellido)   

class ConsultaReclamo(models.Model):
    id = models.AutoField(primary_key=True)
    info_adicional = models.TextField(blank=True)
    consulta = models.BooleanField(default=False)
    reclamo = models.BooleanField(default=False)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {} - {}".format(
            self.fecha.strftime('%Y-%m-%d %H:%M:%S'),
            self.id_persona.nombre,
            self.id_persona.apellido)

    def save(self, *args, **kwargs):
        # Asegurar que solo uno de los campos sea verdadero
        if self.consulta and self.reclamo:
            self.consulta = False
        super().save(*args, **kwargs)

class Animal(models.Model):    
    id = models.AutoField(primary_key=True)
    animal = models.CharField(max_length=20)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(str(self.id), self.animal)

class Adoptar(models.Model):    
    id = models.AutoField(primary_key=True)
    info_adicional = models.TextField(blank=True)
    transito = models.BooleanField(default=False)
    id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id_persona.nombre + ' - ' + self.id_persona.apellido

class TipoCursada(models.Model):    
    id = models.AutoField(primary_key=True)
    tipo_cursada = models.CharField(max_length=20)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(str(self.id), self.tipo_cursada)
    
class Cursos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        estado = "Disponible" if self.disponible else "No Disponible"
        return "{} - {} - {}".format(str(self.id), self.nombre_curso, estado)
    
class Confirmados(models.Model):
    id = models.AutoField(primary_key=True)
    id_cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_tipo_cursada = models.ForeignKey(TipoCursada, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_persona.nombre + ' - ' + self.id_cursos.nombre_curso

class Turno(models.Model):    
    id = models.AutoField(primary_key=True)
    turno = models.CharField(max_length=20)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(str(self.id), self.turno)

class Fechas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    id_turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    info_adicional = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        estado = "Disponible" if self.disponible else "No Disponible"
        return "{} - {} - {}".format(
            self.fecha.strftime('%Y-%m-%d %H:%M:%S'), 
            self.id_turno.turno, 
            estado)

class Colegio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_colegio = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    cant_visitantes = models.IntegerField()
    rango_fechas = models.TextField(blank=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_colegio