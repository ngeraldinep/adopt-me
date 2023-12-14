from django import forms
from .models import Cursos, TipoCursada, Persona, Datos_Personales, Confirmados, ConsultaReclamo, Animal, Adoptar, Colegio, Lazarillo, Turno,Fechas

class FormularioCurso(forms.ModelForm):
    # Datos del Curso - Tabla Confirmados
    nombre_curso = forms.ModelChoiceField(queryset=Cursos.objects.filter(estado=True), label='Nombre del curso')
    modalidad_curso = forms.ModelChoiceField(queryset=TipoCursada.objects.filter(estado=True), label='Modalidad del curso')

    # Datos del usuario - Tablas Persona y Datos_Personales
    nombre = forms.CharField(max_length=30, label='Nombre')
    apellido = forms.CharField(max_length=30, label='Apellido')
    dni = forms.IntegerField(label='DNI')
    telefono = forms.IntegerField(label='Teléfono')
    correo = forms.EmailField(label='Correo electrónico')
    fecha_inscripcion = forms.ModelChoiceField(queryset=Fechas.objects.filter(estado=True), label='Fecha de inscripcion')

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
        )
        persona.id_datospersonales = datos_personales
        persona.save()
        confirmacion.id_cursos = self.cleaned_data['nombre_curso']
        confirmacion.id_tipo_cursada = self.cleaned_data['modalidad_curso']
        confirmacion.id_fechas = self.cleaned_data['fecha_inscripcion']
        confirmacion.id_persona = persona

        if commit:
            confirmacion.save()
        return confirmacion

class FormularioConsultas(forms.ModelForm):
    nombre = forms.CharField(max_length=30, label='Nombre')
    apellido = forms.CharField(max_length=30, label='Apellido')
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
    animal = forms.ModelChoiceField(queryset=Animal.objects.filter(estado=True), label='¿A que animalito quisieras ayudar?')
    
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
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}, format='%d-%m-%Y'),
        }
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
    fecha_visita = forms.ModelChoiceField(queryset=Fechas.objects.filter(estado=True), label='Fecha de visita')
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
                  'fecha_visita', 
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
        confirmacion.id_fechas = self.cleaned_data['fecha_visita']
        
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
   
    id_turno = forms.ModelChoiceField(queryset=Turno.objects.filter(estado=True), label='Turno')
    fecha = forms.DateField(label='Fecha', help_text='Formato: YYYY-MM-DD')
    estado = forms.BooleanField(label='estado', required=False)
    info_adicional = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Fechas 
        fields = ['fecha', 
                  'id_turno', 
                  'estado', 
                  'info_adicional' 
                  ]

    def save(self, commit=True, usuario=None):
        # Guardar los datos relacionados en las tablas correspondientes
        confirmacion = super().save(commit=False)

        confirmacion.id_turno = self.cleaned_data['id_turno']
        
        if usuario:
            confirmacion.usuario = usuario  # Set the usuario field if provided

        if commit:
            confirmacion.save()
        return confirmacion

class FormularioNuevoCurso(forms.ModelForm):
   
    nombre_curso = forms.CharField(max_length=100, label='Nombre del curso o capacitacion')
    estado = forms.BooleanField(label='estado', required=False)

    class Meta:
        model = Cursos 
        fields = ['nombre_curso', 
                  'estado'
                  ]

    def save(self, commit=True, usuario=None):
        # Guardar los datos relacionados en las tablas correspondientes
        confirmacion = super().save(commit=False)
        
        if usuario:
            confirmacion.usuario = usuario  # Set the usuario field if provided

        if commit:
            confirmacion.save()
        return confirmacion