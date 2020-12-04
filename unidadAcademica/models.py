from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UnidadAcademica(models.Model):
    """Unidad Academica Model"""

    NIVELSUPERIOR = 'NS'
    NIVELMEDIOSUPERIOR = 'NMS'

    NIVEL_CHOICES = [
        (NIVELSUPERIOR, 'Nivel Superior'),
        (NIVELMEDIOSUPERIOR,'Nivel Medio Superior'),
    ]

    nombre = models.CharField(max_length=255)
    nivel = models.CharField(
        max_length=3,
        choices=NIVEL_CHOICES,
        blank=True,
        null=True,
        default= NIVELMEDIOSUPERIOR
        )

    id_escuela = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
