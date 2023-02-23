import json
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .validators import *


class NoteDetail(generic.UpdateView):
    model = Note
    template_name = 'note.html'
    form_class = NoteForm

    def get_success_url(self):
        return reverse('mynotes')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password1'),
                # first_name=request.POST.get('first_name'),
                # last_name=request.POST.get('last_name'),
            )
            user.save()
            login(request, user)
            return redirect(reverse('index'))
    else:
        signup_form = SignUpForm()
    return render(request, 'registration/signup.html', context={'form': signup_form})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        signin_form = SignInForm(request.POST)
        if signin_form.is_valid():
            user = authenticate(
                username=signin_form.cleaned_data['username'],
                password=signin_form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Wrong username or password')
                return redirect('signin')
    else:
        signin_form = SignInForm()
    return render(request, 'registration/signin.html', context={'form': signin_form})


def sign_out(request):
    logout(request)
    return redirect(reverse('signin'))


@login_required(login_url='signin/')
def index(request):
    last_notes = Note.objects.filter(author=request.user).order_by('-created')[:3]
    add_form = NoteForm(initial={'title': datetime.now().strftime("%d-%B-%Y (%H:%M)")})
    data = {
        'add_form': add_form,
        'last_notes': last_notes
    }
    if request.method == 'POST':
        try:
            note = Note()
            note.title = request.POST.get('title')
            note.text = request.POST.get('text')
            note.author = request.user
            note.save()
            return HttpResponseRedirect('/')
        except Exception:
            return HttpResponse(status=500)

    return render(request, 'index.html', context=data)


@login_required(login_url='/accounts/login/')
def mynotes(request):
    note_list = Note.objects.filter(author=request.user).order_by('-created')
    data = {
        'note_list': note_list
    }
    return render(request, 'usernotes.html', context=data)


def search(request):
    try:
        note_list = Note.objects.filter(author=request.user).order_by('created')
        search_data = json.load(request)
        results = search_validator(note_list, search_data)
        html = render_to_string('search_results.html', {'results': results})
        return HttpResponse(html)
    except Exception:
        return HttpResponse(status=500)


def delete(request):
    try:
        note_list = Note.objects.filter(author=request.user).order_by('created')
        note_id = json.load(request)['id']
        note = note_list.get(id=note_id)
        note.delete()
        return HttpResponse(status=200)
    except Exception:
        return HttpResponse(status=500)
