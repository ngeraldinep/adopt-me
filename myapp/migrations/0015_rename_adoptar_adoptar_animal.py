# Generated by Django 4.2.5 on 2023-12-10 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_fechas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adoptar',
            old_name='adoptar',
            new_name='animal',
        ),
    ]
