from django.db import models
from etps.models import ETP

# Create your models here.
class Equipo(models.Model):
    """Equipo Model"""

    id_equipo = models.CharField(max_length=50)
    evaluador_originalidad = models.CharField(max_length=50)
    evaluador_estilos = models.CharField(max_length=50)
    evaluador_diseno = models.CharField(max_length=50)
    evaluador_proceso = models.CharField(max_length=50)
    id_etp = models.OneToOneField(ETP, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
