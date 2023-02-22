from django.forms import ModelForm, TextInput, Textarea
from .models import *


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={"rows": "5", 'class': 'form-control'})
        }
        labels = {
            'title': '',
            'text': ''
        }
        help_texts = {
            'title': '',
            'text': ''
        }