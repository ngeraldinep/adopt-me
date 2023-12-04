from django.http import HttpResponse
from .models import Project, Task, FormularioConsultas
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject, FormularioForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


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


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })


def home(request):
    title = 'Adopt-Me!'
    sss = FormularioForm(request.POST)

    if request.method == 'POST':
        if sss.is_valid():
            return render(request, 'home.html', {'sss': sss})
        else:
            FormularioConsultas.objects.create(
                nombre=request.POST['nombre'],
                apellido=request.POST['apellido'],
                telefono=request.POST['telefono'],
                correo=request.POST['correo'],
                # tipo_consulta_reclamo=request.POST['tipo_consulta_reclamo'],
                texto_libre=request.POST['texto_libre']
                # checkbox_llamado=request.POST['checkbox_llamado'],

            )
    return render(request, 'home.html', {'title': title, 'sss': sss})


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


"""     else:
        FormularioConsultas.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            telefono=request.POST['telefono'],
            correo=request.POST['correo'],
            # tipo_consulta_reclamo=request.POST['tipo_consulta_reclamo'],
            texto_libre=request.POST['texto_libre']
            # checkbox_llamado=request.POST['checkbox_llamado'],

        )
        return redirect('home') """

# if request.method == 'POST':
#     form = FormularioForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
# else:
#     form = FormularioForm()

# return render(request, 'home.html', {'form': form})


def registrarme(request):
    title = 'Registrate'
    return render(request, 'registrarme.html', {
        'title': title
    })


def cursoscapacitaciones(request):
    title = 'Capacitaciones e inscripciones'
    return render(request, 'cursoscapacitaciones.html', {
        'title': title
    })


def dondeestamos(request):
    title = 'Donde estamos'
    return render(request, 'dondeestamos.html', {
        'title': title
    })


def historia(request):
    title = 'Nuestra historia'
    return render(request, 'historia.html', {
        'title': title
    })


def adiestramiento(request):
    title = 'Curso de adiestramiento canino'
    return render(request, 'adiestramiento.html', {
        'title': title
    })


def create_form(request):
    title = 'Curso de adiestramiento canino'
    return render(request, 'create_form.html', {
        'title': title
    })


def signup(request):
    title = 'Signup'

    if request.method == 'GET':
        return render(request, 'signup.html', {
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
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no son iguales'
        })
