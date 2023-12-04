from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('home/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('task/', views.task, name="task"),
    path('create_task/', views.create_task, name="create_task"),
    
    path('create_project/', views.create_project, name="create_project"),
    
    path('', views.home, name="home"),
    path('cursoscapacitaciones/', views.cursoscapacitaciones, name="cursoscapacitaciones"),
    path('registrarme/', views.registrarme, name="registrarme"),
    path('dondeestamos/', views.dondeestamos, name="dondeestamos"),
    path('historia/', views.historia, name="historia"),
    path('adiestramiento/', views.adiestramiento, name="adiestramiento"),
    path('create_form/', views.create_form, name="create_form"),
    path('signup/', views.signup, name="Signup"),
    path('logout/', views.logout, name="Logout"),

    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

