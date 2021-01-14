# Generated by Django 3.1.4 on 2021-01-13 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('etps', '0009_auto_20201226_2109'),
        ('equipos', '0002_auto_20201222_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='evaluador_comunicologo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='proceso', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='evaluador_estilos',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='estilos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='evaluador_originalidad',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='originalidad', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='evaluador_pedagogo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='diseno', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='id_etp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='etps.etp'),
        ),
    ]
