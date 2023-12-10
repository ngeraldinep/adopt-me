# Generated by Django 4.2.5 on 2023-12-10 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_adoptar_fecha_consultareclamo_fecha_lazarillo_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('animal', models.CharField(max_length=20)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
    ]