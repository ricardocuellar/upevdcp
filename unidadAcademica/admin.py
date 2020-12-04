#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from django.contrib.auth.models import User
from unidadAcademica.models import UnidadAcademica

# Register your models here.
@admin.register(UnidadAcademica)
class UnidadAcademica(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk', 'nombre','nivel','id_escuela')
    list_filter  = ('nivel','created')

