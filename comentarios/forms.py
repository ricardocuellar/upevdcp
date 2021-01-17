from django import forms
from django.forms import ModelForm

from comentarios.models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta: 
        model=Comentario
        fields=['comentario','etp','evaluador','etpEstado']
        widgets = {'etpEstado': forms.HiddenInput()}
        exclude = ['etp','evaluador']
        