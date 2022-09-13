from django.db import models
from users.models import UsersRole
from etps.models import ETP
from equipos.models import Equipo
# Create your models here.

class Tarea(models.Model):
    """Tareas Model"""

    PENDIENTES = 'Pendientes'
    HACIENDO = 'Haciendo'
    ESPERA = 'Espera'
    HECHO = 'Hecho'

    TAREA_CHOICES = [
        (PENDIENTES , 'Pendientes'),
        (HACIENDO , 'Haciendo'),
        (ESPERA , 'Espera'),
        (HECHO , 'Hecho'),
    ]

    estado_tarea = models.CharField(
        max_length=20,
        choices=TAREA_CHOICES,
        blank=True,
        null=True,
        default= 'Pendientes'
    )

    user_tasks = models.ForeignKey(UsersRole, on_delete=models.CASCADE)
    etp_task = models.ForeignKey(ETP, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)