from django.db import models
from etps.models import ETP
from django.contrib.auth.models import User 

# Create your models here.
class Equipo(models.Model):
    """Equipo Model"""

    evaluador_originalidad = models.ForeignKey(User, related_name='originalidad',on_delete=models.PROTECT)
    evaluador_estilos = models.ForeignKey(User, related_name='estilos', on_delete=models.PROTECT)
    evaluador_pedagogo = models.ForeignKey(User, related_name='diseno', on_delete=models.PROTECT)
    evaluador_comunicologo = models.ForeignKey(User, related_name='proceso', on_delete=models.PROTECT)
    id_etp = models.OneToOneField(ETP, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
