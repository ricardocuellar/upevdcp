# Generated by Django 3.1.4 on 2021-01-16 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0006_auto_20210116_0342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='eptEstado',
            new_name='etpEstado',
        ),
    ]
