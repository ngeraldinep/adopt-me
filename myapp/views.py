from .models import Project, Task, Persona, TipoCursada, Cursos, Confirmados, Datos_Personales, Fechas, Turno
from .forms import CreateNewTask, CreateNewProject, FormularioForm, FormularioCurso, FormularioConsultas, FormularioAdoptar, FormularioVisitas, FormularioLazarillo, FormularioFecha
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RangoFechasForm
from .utils import generar_fechas_automaticas

# from django.shortcuts import get_object_or_404, render


# Create your views here.
def index(request):
    title = 'DJANGO CURSE'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s <h1>" % username)

def about(request):
    username = 'Eric'
    return render(request, 'about.html', {
        'username': username
    })

def fecha(request):
    return render(request, 'notpublic/fecha.html')

def projects(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    project = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'project': project
    })

def task(request):
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse('task: %s ' % task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=2)
        return redirect('task')


def create_project(request):
    form = CreateNewProject(request.POST)
    sss = CreateNewTask(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            # show interface
            return render(request, 'projects/create_project.html', {
                'form': CreateNewProject()
            })
        else:
            Project.objects.create(
                name=request.POST['name'])

        if sss.is_valid():
            sss = CreateNewTask()
            print(sss)
            return render(request, 'projects/create_project.html', {
                'sss': sss
            })
        else:
            Task.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                project_id=2)
    return render(request, 'projects/create_project.html', {'form': form, 'sss': sss})


def create_fecha(request):
    form = FormularioFecha(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            # show interface
            return render(request, 'notpublic/create_fecha.html', {
                'form': FormularioFecha()
            })
        else:
            Project.objects.create(
                name=request.POST['create_fecha'])

    return render(request, 'notpublic/create_fecha.html', {'form': form})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })

def fecha_detail(request, id):
    id = get_object_or_404(Fechas, id=id)
    fecha = Fechas.objects.filter(fecha=fecha)
    turno = Fechas.objects.filter(turno=turno)
    return render(request, 'notpublic/fecha.html', {
        'id': id,
        'fecha': fecha,
        'turno': turno
        # 'tasks': tasks
    })

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
    
def xx(request):
    if request.method == 'POST':
        # show interface
        sss = CreateNewTask()
        print(sss)
        return render(request, 'projects/create_project.html', {
            'sss': sss
        })
    else:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=2)
        return redirect('projects')

def registrarme(request):
    title = 'Registrate'
    return render(request, 'public/formularios/registrarme.html', {
        'title': title
    })

def cursoscapacitaciones(request):
    title = 'Capacitaciones e inscripciones'
    return render(request, 'public/cursoscapacitaciones.html', {
        'title': title
    })

def dondeestamos(request):
    title = 'Donde estamos'
    return render(request, 'public/dondeestamos.html', {
        'title': title
    })

def adoptar(request):
    if request.method == 'POST':
        form = FormularioAdoptar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adopcion')
    else:
        form = FormularioAdoptar()

    return render(request, 'public/formularios/adopcion.html', {'form': form})   

def historia(request):
    title = 'Nuestra historia'
    return render(request, 'public/historia.html', {
        'title': title
    })

def adiestramiento(request):
    if request.method == 'POST':
        form = FormularioCurso(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adiestramiento')
    else:
        form = FormularioCurso()

    return render(request, 'public/formularios/adiestramiento.html', {'form': form})   

def visitas(request):
    if request.method == 'POST':
        form = FormularioVisitas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitas')
    else:
        form = FormularioVisitas()

    return render(request, 'public/formularios/visitas.html', {'form': form})   

def lazarillo(request):
    if request.method == 'POST':
        form = FormularioLazarillo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lazarillo')
    else:
        form = FormularioLazarillo()

    return render(request, 'public/formularios/lazarillo.html', {'form': form})   

def create_form(request):
    title = 'Curso de adiestramiento canino'
    return render(request, 'public/formularios/create_form.html', {
        'title': title
    })
    
def pago(request):
    title = 'Donaciones / Pagos'
    return render(request, 'public/formularios/donacionpago.html', {
        'title': title
    })

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

def generar_fechas(request):
    if request.method == 'POST':
        form = RangoFechasForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            usuario_logueado = request.user.username
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            print(f"Usuario: {usuario_logueado}, Inicio: {fecha_inicio}, Fin: {fecha_fin}")
            fechas_generadas = generar_fechas_automaticas(usuario_logueado, fecha_inicio, fecha_fin)
            print(f"Fechas generadas: {fechas_generadas}")
            return HttpResponse("Fechas generadas correctamente")
        else:
            print("Form is not valid")
            form = RangoFechasForm()

    return render(request, 'notpublic/generar_fechas.html', {'form': form})