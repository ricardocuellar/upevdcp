# Generated by Django 3.1.4 on 2021-01-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0004_auto_20210115_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='revisado',
            field=models.BooleanField(default=0),
        ),
    ]
