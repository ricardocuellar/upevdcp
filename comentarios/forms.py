from django.forms import ModelForm
from comentarios.models import Comentario

class ComentarioForm(ModelForm):
    class Meta: 
        model=Comentario
        fields=['comentario','etp','evaluador']
        exclude = ['etp','evaluador']