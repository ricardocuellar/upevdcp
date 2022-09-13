from django.db import models

from carreras.models import Carrera

# Create your models here.

class Materia(models.Model):
    """Materia Model"""

    nombre = models.CharField(max_length=255)
    id_materia = models.CharField(max_length=128)
    carreras = models.ManyToManyField(Carrera)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
