#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from django.contrib.auth.models import User
from carreras.models import Carrera
from materias.models import Materia

# Register your models here.
@admin.register(Materia)
class Materia(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk', 'nombre','id_materia','get_carreras')
    list_display_links = ('pk','nombre')
    list_filter  = ('created','nombre')


    def get_carreras(self, obj):
        return list(obj.carreras.all())



    
    readonly_fields = ('created', 'modified')
