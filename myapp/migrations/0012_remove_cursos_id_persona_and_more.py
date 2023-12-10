# Generated by Django 4.2.5 on 2023-12-09 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_cursos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='id_persona',
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='id_tipo_cursada',
        ),
        migrations.CreateModel(
            name='Confirmados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_cursos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cursos')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.persona')),
                ('id_tipo_cursada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tipocursada')),
            ],
        ),
    ]