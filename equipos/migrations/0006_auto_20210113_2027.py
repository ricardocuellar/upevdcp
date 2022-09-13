# Generated by Django 3.1.4 on 2021-01-14 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipos', '0005_auto_20210113_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='evaluador_comunicologo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='proceso', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='evaluador_estilos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estilos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='evaluador_originalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='originalidad', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='evaluador_pedagogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='diseno', to=settings.AUTH_USER_MODEL),
        ),
    ]
