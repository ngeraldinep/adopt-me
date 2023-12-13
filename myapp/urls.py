from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .models import ConsultaReclamo, Adoptar, Lazarillo, Confirmados, Colegio, Fechas, Cursos


urlpatterns = [
    # Paths para usuarios NO REGISTRADOS
    path('', views.home, name="home"),
    path('dondeestamos/', views.dondeestamos, name="dondeestamos"),
    path('historia/', views.historia, name="historia"),
    path('capacitacioneseinscripciones/', views.capacitacioneseinscripciones, name="capacitacioneseinscripciones"),
    
    # Path de Formularios para usuario NO REGISTRADOS
    path('formulario/cursosycapacitaciones/', views.cursosycapacitaciones, name="cursosycapacitaciones"),
    path('formulario/visitas/', views.visitas, name="visitas"),
    path('formulario/lazarillo/', views.lazarillo, name="lazarillo"),
    path('formulario/adopcion/', views.adoptar, name="adopcion"),
    path('formulario/donacionpago/', views.pago, name="donacionpago"),
    
    # Path de Registro, login y logout
    path('formulario/signup/', views.signup, name="Signup"),
    path('formulario/signin/', views.signin, name="signin"),
    path('formulario/logout/', views.signout, name="Logout"),
    
    # Paths para usuarios REGISTRADOS

    # Path de Formularios para usuario REGISTRADOS
    path('notpublic/create_fecha/', views.create_fecha, name="create_fecha"),
    path('notpublic/create_curso/', views.create_curso, name="create_curso"),

    # Paths de Consultas y Cambio de Estado 
    path('notpublic/consulta_detail/', views.filter_and_render, {'model_class': ConsultaReclamo, 'template_name': 'notpublic/consulta_pendiente.html'}, name='consulta_detail'),
    path('notpublic/change_estado/<int:id>/', views.change_estado, name='change_estado'),
    
    path('notpublic/adoptar_detail/', views.filter_and_render, {'model_class': Adoptar, 'template_name': 'notpublic/consulta_adopcion.html'}, name='adoptar_detail'),
    path('notpublic/change_adopcion/<int:id>/', views.change_adopcion, name='change_adopcion'),
    
    path('notpublic/lazarillo_detail/', views.filter_and_render, {'model_class': Lazarillo, 'template_name': 'notpublic/consulta_lazarillo.html'}, name='lazarillo_detail'),
    path('notpublic/change_lazarillo/<int:id>/', views.change_lazarillo, name='change_lazarillo'),
    
    path('notpublic/inscripciones_detail/', views.filter_and_render, {'model_class': Confirmados, 'template_name': 'notpublic/consulta_inscripciones.html'}, name='inscripciones_detail'),
    path('notpublic/change_inscripciones/<int:id>/', views.change_inscripciones, name='change_inscripciones'),
    
    path('notpublic/visitas_detail/', views.filter_and_render, {'model_class': Colegio, 'template_name': 'notpublic/consulta_visitas.html'}, name='visitas_detail'),
    path('notpublic/change_visitas/<int:id>/', views.change_visitas, name='change_visitas'),
    
    path('notpublic/fechas_detail/', views.filter_and_render, {'model_class': Fechas, 'template_name': 'notpublic/consulta_fechas.html'}, name='fechas_detail'),
    path('notpublic/change_fechas/<int:id>/', views.change_fechas, name='change_fechas'),
    
    path('notpublic/cursosycapacitaciones_detail/', views.filter_and_render, {'model_class': Cursos, 'template_name': 'notpublic/consulta_cursosycapacitaciones.html'}, name='cursosycapacitaciones_detail'),
    path('notpublic/change_cursosycapacitaciones/<int:id>/', views.change_cursosycapacitaciones, name='change_cursosycapacitaciones'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

