# Generated by Django 4.2.5 on 2023-12-12 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_consultareclamo_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptar',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='colegio',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='confirmados',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lazarillo',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]