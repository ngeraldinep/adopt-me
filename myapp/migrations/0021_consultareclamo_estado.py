# Generated by Django 4.2.5 on 2023-12-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_turno_remove_fechas_turno_fechas_id_turno'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultareclamo',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
