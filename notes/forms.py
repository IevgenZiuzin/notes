from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import ModelForm, TextInput, Textarea
from .models import *


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={"rows": "5", 'class': 'form-control'}),
        }
        labels = {
            'title': '',
            'text': '',
        }
        help_texts = {
            'title': '',
            'text': '',
        }


class SignUpForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        min_length=2,
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    # first_name = forms.CharField(
    #     required=False,
    #     label='Firstname',
    #     max_length=20,
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control'}
    #     )
    # )
    # last_name = forms.CharField(
    #     required=False,
    #     label='Lastname',
    #     max_length=20,
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control'}
    #     )
    # )
    password1 = forms.CharField(
        required=True,
        label='Password',
        min_length=4,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        required=True,
        label='Confirm password',
        min_length=4,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2


class SignInForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'username',
                   }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password',
            })
    )