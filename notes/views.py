import json
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
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
        view_name = 'mynotes'
        return reverse(view_name)


@login_required(login_url='/accounts/login/')
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
