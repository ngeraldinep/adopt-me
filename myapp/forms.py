from django import forms
from .models import Cursos, TipoCursada, Persona, Datos_Personales, Confirmados, ConsultaReclamo, Animal, Adoptar, Colegio, Lazarillo, Turno,Fechas

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo tarea", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea(attrs={'class':'input'}))
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre poryecto", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    
class FormularioForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=30, widget=forms.TextInput(attrs={'class':'input'}))
    apellido = forms.CharField(label="Apellido", max_length=30, widget=forms.TextInput(attrs={'class':'input'}))
    telefono = forms.CharField(label="Número de Celular", max_length=8, widget=forms.TextInput(attrs={'class':'input'}))    
    correo = forms.EmailField(max_length = 200)      
    #tipo_consulta_reclamo = forms.CharField(required=True)(label="Tipo", widget=forms.Select(attrs={'class':'input'}))
    texto_libre = forms.CharField(label="Texto", widget=forms.Textarea(attrs={'class':'input'}))    
    #checkbox_llamado = forms.RadioSelect(widget=forms.RadioSelect())     
    
    # class Meta:
    #     model = Formulario_consultas
    #     fields = ['nombre', 'apellido', 'telefono', 'correo', 'tipo_consulta_reclamo', 'texto_libre', 'checkbox_llamado']
    #     widgets = {'tipo_consulta_reclamo': forms.Select(attrs={'class': 'form-control'}),}

class FormularioCurso(forms.ModelForm):
    # Datos del Curso - Tabla Confirmados
    nombre_curso = forms.ModelChoiceField(queryset=Cursos.objects.filter(disponible=True), label='Nombre del curso')
    modalidad_curso = forms.ModelChoiceField(queryset=TipoCursada.objects.filter(disponible=True), label='Modalidad del curso')

    # Datos del usuario - Tablas Persona y Datos_Personales
    nombre = forms.CharField(max_length=30, label='Nombre')
    apellido = forms.CharField(max_length=30, label='Apellido')
    dni = forms.IntegerField(label='DNI')
    telefono = forms.IntegerField(label='Teléfono')
    correo = forms.EmailField(label='Correo electrónico')
    fecha_inscripcion = forms.DateField(label='Fecha de inscripción')

    class Meta:
        model = Confirmados
        fields = ['nombre_curso', 'modalidad_curso', 'nombre', 'apellido', 'dni', 'telefono', 'correo', 'fecha_inscripcion']

    def save(self, commit=True):
        # Guardar los datos relacionados en las tablas correspondientes
        confirmacion = super().save(commit=False)
        persona = Persona.objects.create(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            telefono=self.cleaned_data['telefono'],
            correo=self.cleaned_data['correo']
        )
        datos_personales = Datos_Personales.objects.create(
            dni=self.cleaned_data['dni'],
            fecha_nacimiento=self.cleaned_data['fecha_inscripcion'],
            id_persona=persona
        )
        confirmacion.id_cursos = self.cleaned_data['nombre_curso']
        confirmacion.id_tipo_cursada = self.cleaned_data['modalidad_curso']
        confirmacion.id_persona = persona

        if commit:
            confirmacion.save()
        return confirmacion

class FormularioConsultas(forms.ModelForm):
    # Consulta/Reclamo - Tabla Confirmados
    # Datos del usuario - Tablas Persona
    nombre = forms.CharField(max_length=30, label='Nombre')
    apellido = forms.CharField(max_length=30, label='Apellido')
    # fecha = forms.DateField(label='Fecha de inscripción')
    telefono = forms.IntegerField(label='Teléfono')
    correo = forms.EmailField(label='E-Mail')
    info_adicional = forms.CharField(required=False, widget=forms.Textarea)
    OPCIONES_CONSULTA_RECLAMO = [
        (False, 'Consulta'),
        (True, 'Reclamo'),
    ]

    consulta_reclamo = forms.ChoiceField(
        label='Tipo',
        choices=OPCIONES_CONSULTA_RECLAMO,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        initial=False
    )
   
    class Meta:
        model = ConsultaReclamo
        fields = ['nombre', 'apellido', 'telefono', 'correo', 'info_adicional','consulta_reclamo' ]

    def save(self, commit=True):
        # Guardar los datos relacionados en las tablas correspondientes
        confirmacion = super().save(commit=False)
        persona = Persona.objects.create(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            telefono=self.cleaned_data['telefono'],
            correo=self.cleaned_data['correo']
        )

        confirmacion.id_persona = persona
        confirmacion.consulta = (self.cleaned_data['consulta_reclamo'] == 'False')
        confirmacion.reclamo = (self.cleaned_data['consulta_reclamo'] == 'True')
        
        if commit:
            confirmacion.save()
        return confirmacion

class FormularioAdoptar(forms.ModelForm):
    # Datos Persona - Tabla Persona y Datos_Personales
    nombre = forms.CharField(max_length=30, label='Nombre')
    apellido = forms.CharField(max_length=30, label='Apellido')
    dni = forms.IntegerField(label='DNI')
    fecha_nacimiento  = forms.DateField(label='Fecha de Nacimiento')
    telefono = forms.IntegerField(label='Teléfono')
    correo = forms.EmailField(label='E-Mail')
    
    # Datos animal - Tabla animal
    animal = forms.ModelChoiceField(queryset=Animal.objects.filter(disponible=True), label='¿A que animalito quisieras ayudar?')
    
    # Datos Adopcio - Tabla Adoptar
    info_adicional = forms.CharField(required=False, widget=forms.Textarea)
    
    OPCIONES_ADOPCION = [
        (False, 'Adopción'),
        (True, 'Transito'),
    ]

    consulta_transito = forms.ChoiceField(
        label='Tipo',
        choices=OPCIONES_ADOPCION,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        initial=False)

    # Armado del Formulario
    class Meta:
        model = Adoptar
        fields = ['nombre', 'apellido', 'dni', 'fecha_nacimiento','telefono', 'correo', 'animal', 'info_adicional','consulta_transito' ]
    # Guardado del del Formulario
    def save(self, commit=True):
        # Guardar los datos relacionados en las tablas correspondientes
        confirmacion = super().save(commit=False)
        persona = Persona.objects.create(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            telefono=self.cleaned_data['telefono'],
            correo=self.cleaned_data['correo']
        )
        datos_personales = Datos_Personales.objects.create(
            dni=self.cleaned_data['dni'],
            fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
            id_persona=persona
        )
        confirmacion.id_persona = persona
        confirmacion.id_animal = self.cleaned_data['animal']
        confirmacion.transito = self.cleaned_data['consulta_transito']
        
        if commit:
            confirmacion.save()
        return confirmacion

class FormularioVisitas(forms.ModelForm):
    # Consulta/Reclamo - Tabla Confirmados
    
    nombre_colegio = forms.CharField(max_length=100, label='Nombre de la institucion')
    cargo = forms.CharField(max_length=50, label='Cargo')
    cant_visitantes = forms.IntegerField(label='Cantidad de visitantes')
    rango_fechas  = forms.CharField(required=False, widget=forms.Textarea)
    # Datos del usuario - Tablas Persona
    nombre = forms.CharField(max_length=30, label='Nombre')
    apellido = forms.CharField(max_length=30, label='Apellido')
    telefono = forms.IntegerField(label='Teléfono')
    correo = forms.EmailField(label='E-Mail')
    
    class Meta:
        model = Colegio
        fields = ['nombre_colegio', 
                  'cargo', 
                  'cant_visitantes', 
                  'rango_fechas', 
                  'nombre', 
                  'apellido', 
                  'telefono', 
                  'correo']

    def save(self, commit=True):
        # Guardar los datos relacionados en las tablas correspondientes
        confirmacion = super().save(commit=False)
        persona = Persona.objects.create(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            telefono=self.cleaned_data['telefono'],
            correo=self.cleaned_data['correo']
        )

        confirmacion.id_persona = persona
        
        if commit:
            confirmacion.save()
        return confirmacion
    
class FormularioLazarillo(forms.ModelForm):
    # Datos del usuario - Tablas Persona
    nombre = forms.CharField(max_length=30, label='Nombre')
    apellido = forms.CharField(max_length=30, label='Apellido')
    telefono = forms.IntegerField(label='Teléfono')
    correo = forms.EmailField(label='E-Mail')
    
    # Lazarillo - Tabla Lazarillo
    discapacidad  = forms.CharField(max_length=100, label='Tipo de discapacidad')
    primer_lazarillo = forms.BooleanField(label='Primer Lazarillo', required=False)
    info_adicional  = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Lazarillo 
        fields = ['nombre', 
                  'apellido', 
                  'telefono', 
                  'correo',
                  'discapacidad', 
                  'primer_lazarillo', 
                  'info_adicional' 
                  ]

    def save(self, commit=True):
        # Guardar los datos relacionados en las tablas correspondientes
        confirmacion = super().save(commit=False)
        persona = Persona.objects.create(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            telefono=self.cleaned_data['telefono'],
            correo=self.cleaned_data['correo']
        )

        confirmacion.id_persona = persona
        
        if commit:
            confirmacion.save()
        return confirmacion

class FormularioFecha(forms.ModelForm):
   
    id_turno = forms.ModelChoiceField(queryset=Turno.objects.filter(disponible=True), label='Turno')
   
    # Fecha - Tabla Fechas
    fecha = forms.DateField(label='Fecha')
    disponible = forms.BooleanField(label='Disponible', required=False)
    info_adicional = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Fechas 
        fields = ['fecha', 
                  'id_turno', 
                  'disponible', 
                  'info_adicional' 
                  ]

    def save(self, commit=True):
        # Guardar los datos relacionados en las tablas correspondientes
        confirmacion = super().save(commit=False)

        confirmacion.id_turno = self.cleaned_data['id_turno']
        
        if commit:
            confirmacion.save()
        return confirmacion
    
class RangoFechasForm(forms.Form):
    fecha_inicio = forms.DateField(label='Fecha de inicio')
    fecha_fin = forms.DateField(label='Fecha de fin')