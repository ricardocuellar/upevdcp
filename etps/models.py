from django.db import models
from materias.models import Materia

# Create your models here.
class ETP(models.Model):
    """ETP Model"""

    ORIGINALIDAD = 'Originalidad'
    ESTILOS = 'Estilos'
    DISENO = 'Diseño'
    PROCESO = 'Proceso'
    TERMINADO = 'Terminado'

    ESTADO_CHOICES = [
        (ORIGINALIDAD , 'Originalidad'),
        (ESTILOS , 'Estilos'),
        (DISENO , 'Diseño'),
        (PROCESO , 'Proceso'),
        (TERMINADO , 'Terminado'),
    ]

    oficio = models.IntegerField()
    materia = models.OneToOneField(Materia, on_delete=models.CASCADE)
    id_upev = models.IntegerField()
    usuario_plataforma = models.CharField(max_length=70)
    password_plataforma = models.CharField(max_length=70)
    revision = models.PositiveSmallIntegerField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        blank=True,
        null=True,
        default= '-'
        )

    solicitud_aprobada = models.BooleanField()
    terminado = models.BooleanField()


    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)