from django.db import models
from django.contrib.auth.models import User
from materias.models import Materia

# Create your models here.
class ETP(models.Model):
    """ETP Model"""

    ORIGINALIDAD = 'Originalidad'
    PEDAGOGICO = 'Pedagógico'
    COMUNICACION = 'Comunicación'
    ESTILOS = 'Estilos'
    TECNICOS = 'Técnicos'
    PROCESO = 'Proceso'
    ESPERA = 'Espera'
    TERMINADO = 'Terminado'

    ESTADO_CHOICES = [
        (ORIGINALIDAD , 'Originalidad'),
        (PEDAGOGICO , 'Pedagógico'),
        (COMUNICACION , 'Comunicación'),
        (ESTILOS , 'Estilos'),
        (TECNICOS , 'Técnicos'),
        (PROCESO , 'Proceso'),
        (ESPERA , 'Espera'),
        (TERMINADO , 'Terminado'),
    ]

    oficio = models.IntegerField()
    materia = models.OneToOneField(Materia, on_delete=models.CASCADE)
    id_upev = models.IntegerField(default=0)
    usuario_plataforma = models.CharField(max_length=70)
    password_plataforma = models.CharField(max_length=70)
    revision = models.PositiveSmallIntegerField(default=0)

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        blank=True,
        null=True,
        default= 'Proceso'
        )

    solicitud_aprobada = models.BooleanField(default=0)
    terminado = models.BooleanField(default=0)
    pendientes = models.BooleanField(default=0)
    solicitante =  models.ForeignKey(User, on_delete=models.CASCADE)
    documento = models.FileField(upload_to='solicitudes/etp/')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)