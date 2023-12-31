# Generated by Django 4.2.5 on 2023-12-04 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_tipoconsultareclamo_formulario_consultas'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioConsultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=8)),
                ('correo', models.EmailField(max_length=254)),
                ('texto_libre', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Formulario_consultas',
        ),
    ]
