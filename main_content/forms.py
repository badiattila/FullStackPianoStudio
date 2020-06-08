from django import forms
from .models import Pianos

class PianosPostForm(forms.ModelForm):
    class Meta:
        model = Pianos
        fields = ('brand', 'price', 'age', 'description', 'image')
