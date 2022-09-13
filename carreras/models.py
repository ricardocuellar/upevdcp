from django.db import models
from unidadAcademica.models import UnidadAcademica
# Create your models here.


class Carrera(models.Model):
    """Carreras Model"""

    FISICOMATEMATICO = 'FM'
    MEDICOBIOLOGICAS = 'MB'
    CIENCIASSOCIALES = 'CS'
    OTROS = 'OT'

    AREA_CHOICES = [
        (FISICOMATEMATICO , 'FM'),
        (MEDICOBIOLOGICAS , 'MB'),
        (CIENCIASSOCIALES , 'CS'),
        (OTROS , 'OT')
    ]

    nombre = models.CharField(max_length=255)
    area = models.CharField(
        max_length=3,
        choices=AREA_CHOICES,
        blank=True,
        null=True,
        default= '-'
        )

    id_carrera = models.CharField(max_length=128)
    unidadacademica = models.ForeignKey(UnidadAcademica, on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
