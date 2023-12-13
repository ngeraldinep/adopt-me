from .models import Persona, TipoCursada, Cursos, Confirmados, Datos_Personales, Fechas, Turno, ConsultaReclamo, Adoptar, Lazarillo, Colegio
from .forms import FormularioCurso, FormularioConsultas, FormularioAdoptar, FormularioVisitas, FormularioLazarillo, FormularioFecha, FormularioNuevoCurso
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def hello(request, username):
    return HttpResponse("<h1>Hello %s <h1>" % username)

def home(request):
    title = 'Adopt-Me!'
    if request.method == 'POST':
        form = FormularioConsultas(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulario enviado exitosamente.')  # Agrega esta línea para mostrar el mensaje
            return redirect('home')
    else:
        form = FormularioConsultas()

    return render(request, 'home.html', {'form': form, 'title': title})     

def capacitacioneseinscripciones(request):
    title = 'Capacitaciones e inscripciones'
    return render(request, 'public/capacitacioneseinscripciones.html', {
        'title': title
    })

def dondeestamos(request):
    title = 'Donde estamos'
    return render(request, 'public/dondeestamos.html', {
        'title': title
    })

def historia(request):
    title = 'Nuestra historia'
    return render(request, 'public/historia.html', {
        'title': title
    })

def pago(request):
    title = 'Donaciones / Pagos'
    return render(request, 'public/formularios/donacionpago.html', {
        'title': title
    })

# Formularios Publicos
def visitas(request):
    if request.method == 'POST':
        form = FormularioVisitas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capacitacioneseinscripciones')
    else:
        form = FormularioVisitas()

    return render(request, 'public/formularios/visitas.html', {'form': form})   

def lazarillo(request):
    if request.method == 'POST':
        form = FormularioLazarillo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capacitacioneseinscripciones')
    else:
        form = FormularioLazarillo()

    return render(request, 'public/formularios/lazarillo.html', {'form': form})   
    
def adoptar(request):
    if request.method == 'POST':
        form = FormularioAdoptar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capacitacioneseinscripciones')
    else:
        form = FormularioAdoptar()

    return render(request, 'public/formularios/adopcion.html', {'form': form})   

def cursosycapacitaciones(request):
    if request.method == 'POST':
        form = FormularioCurso(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capacitacioneseinscripciones')
    else:
        form = FormularioCurso()

    return render(request, 'public/formularios/cursosycapacitaciones.html', {'form': form})   

# Formulario No Publico
def create_fecha(request):
    if request.method == 'POST':
        form = FormularioFecha(request.POST)   
        if form.is_valid():
            # Save the form data to create a new Fechas object
            fecha_obj = form.save(commit=False)
            fecha_obj.usuario = request.user  # Assuming you have a user associated with the request
            fecha_obj.save()
            return redirect('create_fecha')  # Redirect to the same page after successful form submission
    else:
        form = FormularioFecha()

    return render(request, 'notpublic/create_fecha.html', {'form': form})

def create_curso(request):
    if request.method == 'POST':
        form = FormularioNuevoCurso(request.POST)   
        if form.is_valid():
            # Save the form data to create a new Fechas object
            fecha_obj = form.save(commit=False)
            fecha_obj.usuario = request.user  # Assuming you have a user associated with the request
            fecha_obj.save()
            return redirect('create_curso')  # Redirect to the same page after successful form submission
    else:
        form = FormularioNuevoCurso()

    return render(request, 'notpublic/create_curso.html', {'form': form})

# Logeo y Registro

def signout(request):
    logout(request)
    return redirect('home')

def signup(request):
    title = 'Signup'

    if request.method == 'GET':
        return render(request, 'log/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Registrar usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'log/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'log/signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no son iguales'
        })

def signin(request):
    
    if request.method == 'GET':
        return render(request, 'log/signin.html', {
            'form' : AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'log/signin.html', {
                'form' : AuthenticationForm,
                'error' : 'Usuario o Contraseña incorrectos!'
            })
        else:
            login(request, user)
            return redirect('home')

# Filtro y cambios de estado

def filter_and_render(request, model_class, template_name):
    # Get filter parameter
    filtro = request.GET.get('estado_filtrar', None)
    
    # Check if filtro is not empty and is a valid integer
    if filtro is not None and filtro.isdigit():
        filtro = bool(int(filtro))  # Convert to boolean
    else:
        filtro = None  # Set to None if it's empty or not a valid integer

    # Initial queryset
    datos = model_class.objects.all()

    # Apply filtering if a filtro is provided
    if filtro is not None:
        datos = datos.filter(estado=filtro)

    return render(request, template_name, {
        'datos': datos,
    })
    
def change_status(request, id, model_class, redirect_target):
    instance = get_object_or_404(model_class, id=id)
    estado_filtrar = None

    if hasattr(instance, 'estado'):
        estado_filtrar = 'estado'
    # elif hasattr(instance, 'estado'):
    #     estado_filtrar = 'estado'
    # elif hasattr(instance, 'estado'):
    #     estado_filtrar = 'estado'

    if estado_filtrar is not None:
        setattr(instance, estado_filtrar, not getattr(instance, estado_filtrar))  # Toggle the status field
        instance.save()
    return redirect(redirect_target)

def change_adopcion(request, id):
    return change_status(request, id, Adoptar, 'adoptar_detail')

def change_estado(request, id):
    return change_status(request, id, ConsultaReclamo, 'consulta_detail')

def change_lazarillo(request, id):
    return change_status(request, id, Lazarillo, 'lazarillo_detail')

def change_inscripciones(request, id):
    return change_status(request, id, Confirmados, 'inscripciones_detail')

def change_visitas(request, id):
    return change_status(request, id, Colegio, 'visitas_detail')

def change_fechas(request, id):
    return change_status(request, id, Fechas, 'fechas_detail')

def change_cursosycapacitaciones(request, id):
    return change_status(request, id, Cursos, 'cursosycapacitaciones_detail')