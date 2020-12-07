"""User Models"""

#Django
from django.contrib.auth.models import User
from django.db import models


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

    role = models.CharField(
        max_length=9,
        choices=ROLE_CHOICES,
        blank=True,
        null=True,
        default= PERSONALUPEV
        )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     """Return username"""
    #     return self.user.username
    

    
