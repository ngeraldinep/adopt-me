# Generated by Django 4.2.5 on 2023-11-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_cursos'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
    ]
