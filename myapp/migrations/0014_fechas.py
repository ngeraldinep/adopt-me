# Generated by Django 4.2.5 on 2023-12-10 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0013_lazarillo_consultareclamo_colegio_adoptar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fechas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(null=True)),
                ('turno', models.CharField(max_length=50)),
                ('disponible', models.BooleanField(default=True)),
                ('info_adicional', models.TextField(blank=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
