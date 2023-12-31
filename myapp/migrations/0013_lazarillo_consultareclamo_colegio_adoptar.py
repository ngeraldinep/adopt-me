# Generated by Django 4.2.5 on 2023-12-10 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0012_remove_cursos_id_persona_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lazarillo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('info_adicional', models.TextField(blank=True)),
                ('discapacidad', models.CharField(max_length=30)),
                ('primer_lazarillo', models.BooleanField(default=False)),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.persona')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultaReclamo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('info_adicional', models.TextField(blank=True)),
                ('consulta', models.BooleanField(default=False)),
                ('reclamo', models.BooleanField(default=False)),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_colegio', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=50)),
                ('cant_visitantes', models.IntegerField()),
                ('rango_fechas', models.TextField(blank=True)),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.persona')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Adoptar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('info_adicional', models.TextField(blank=True)),
                ('transito', models.BooleanField(default=False)),
                ('adoptar', models.CharField(max_length=30)),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.persona')),
            ],
        ),
    ]
