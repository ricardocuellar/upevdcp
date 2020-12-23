from django.db import models
from etps.models import ETP
from django.contrib.auth.models import User 

# Create your models here.
class Equipo(models.Model):
    """Equipo Model"""

    id_equipo = models.CharField(max_length=50)
    evaluador_originalidad = models.OneToOneField(User, related_name='originalidad', on_delete=models.CASCADE)
    evaluador_estilos = models.OneToOneField(User, related_name='estilos', on_delete=models.CASCADE)
    evaluador_pedagogo = models.OneToOneField(User, related_name='diseno', on_delete=models.CASCADE)
    evaluador_comunicologo = models.OneToOneField(User, related_name='proceso', on_delete=models.CASCADE)
    id_etp = models.OneToOneField(ETP, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
