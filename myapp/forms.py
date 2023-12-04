from django import forms

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