# Generated by Django 4.2.5 on 2023-12-13 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_rename_disponible_animal_estado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
