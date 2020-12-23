"""User Models"""

#Django
from django.contrib.auth.models import User
from django.db import models

#Models 
from unidadAcademica.models import UnidadAcademica

# Create your models here.

class UsersRole(models.Model):
    """ Profile model.
    Proxy model that extends the base data with other information"""

    #user extensio
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Users role
    COORDINADORUPEV = 'admin'
    COORDINADORUTEYCV = 'uteycv'
    PERSONALUPEV = 'evaluador'

    ROLE_CHOICES = [
        (COORDINADORUPEV, 'CoordinadorUPEV'),
        (COORDINADORUTEYCV,'CoordinadorUTEyCV'),
        (PERSONALUPEV, 'PersonalUPEV')
    ]

    #Evaluadores positions
    ORIGINALIDAD = 'originalidad'
    ESTILOS = 'estilos'
    PEDAGOGO = 'pedagogo'
    COMUNICOLOGO = 'comunicologo'
    NINGUNO = 'ninguno'

    EVALUADORES_CHOICES = [
        (ORIGINALIDAD , 'Originalidad'),
        (ESTILOS , 'Estilos'),
        (PEDAGOGO , 'Pedagogo'),
        (COMUNICOLOGO , 'Comunicologo'),
        (NINGUNO, 'Ninguno')
    ]

    role = models.CharField(
        max_length=9,
        choices=ROLE_CHOICES,
        blank=True,
        null=True,
        default= PERSONALUPEV
        )
    
    evaluador = models.CharField(
        max_length=12,
        choices=EVALUADORES_CHOICES,
        blank=True,
        null=True,
        default= NINGUNO
    )

    unidad_academica = models.OneToOneField(UnidadAcademica, on_delete=models.CASCADE, blank=True, null=True)

    disponible = models.BooleanField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     """Return username"""
    #     return self.user.username
    

    
