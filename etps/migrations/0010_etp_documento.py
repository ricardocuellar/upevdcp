# Generated by Django 3.1.4 on 2021-01-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etps', '0009_auto_20201226_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='etp',
            name='documento',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]
