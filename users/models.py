"""User Models"""

#Django
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    """ Profile model.
    Proxy model that extends the base data with other information"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
