from django import forms
from datetime import datetime


class NoteForm(forms.Form):
    title = forms.CharField(
        required=True,
        label='Title',
        initial=datetime.now().strftime("%d-%m-%Y (%H:%M)"),
    )
    text = forms.CharField(
        required=False,
        label='Text',
        widget=forms.Textarea(attrs={"rows": "5"})
    )


class SearchForm(forms.Form):
    search_match = forms.CharField(
        label='Search match',
        required=False,
    )
    date_from = forms.DateField(
        label='from',
        required=False,
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )
    date_to = forms.DateField(
        label='to',
        required=False,
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )