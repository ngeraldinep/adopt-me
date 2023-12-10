# Generated by Django 4.2.5 on 2023-12-05 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_formularioconsultas_delete_formulario_consultas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCursada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cursada', models.CharField(max_length=20)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cursos',
        ),
        migrations.DeleteModel(
            name='FormularioConsultas',
        ),
        migrations.DeleteModel(
            name='TipoConsultaReclamo',
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]