"""Post forms"""

#Django
from django import forms

# Models
from etps.models import ETP
from equipos.models import Equipo
from users.models import UsersRole

class ETPForm(forms.ModelForm):
    """ETP model form"""
    class Meta: 
        """Form settigns"""
        model = ETP
        fields = ('oficio','materia','usuario_plataforma','password_plataforma','solicitante','documento')
        exclude = ['solicitante']



class EquipoForm(forms.ModelForm):
    """Create Team Model form"""
    class Meta:
        """Form settings"""
        model = Equipo
        fields = ('id_equipo','evaluador_originalidad','evaluador_estilos','evaluador_pedagogo','evaluador_comunicologo','id_etp')

