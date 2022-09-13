#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from django.contrib.auth.models import User
from carreras.models import Carrera
from unidadAcademica.models import UnidadAcademica

# Register your models here.
@admin.register(Carrera)
class Carrera(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk', 'nombre','area','id_carrera','get_unidadacademica')
    list_display_links = ('pk','nombre')
    list_filter  = ('area','created')


    def get_unidadacademica(self, obj):
        return UnidadAcademica.objects.get(pk=obj.unidadacademica_id).nombre


    
    readonly_fields = ('created', 'modified')


