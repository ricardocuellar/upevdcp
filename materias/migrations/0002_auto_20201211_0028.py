# Generated by Django 3.1.4 on 2020-12-11 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materia',
            old_name='materias',
            new_name='carreras',
        ),
    ]
