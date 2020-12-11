"""Post forms"""

#Django
from django import forms

# Models

from etps.models import ETP

class ETPForm(forms.ModelForm):
    """Post model form"""
    class Meta: 
        """Form settigns"""
        model = Post
        fields = ('materia', 'profile', 'title', 'photo')


