from django import forms
from datetime import datetime


class NoteForm(forms.Form):
    title = forms.CharField(
        required=True,
        initial=datetime.now().strftime("%d-%m-%Y (%H:%M)"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": "5", 'class': 'form-control'})
    )


class SearchForm(forms.Form):
    search_match = forms.CharField(
        label='Search match',
        required=False,
        initial='asdf'
    )
    date_from = forms.DateField(
        label='from',
        required=False,
        initial='2023-02-13',
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