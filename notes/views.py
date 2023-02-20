import json

from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .validators import *

# XAePpQkZOM


class NoteDetail(generic.UpdateView):
    model = Note
    fields = ['title', 'text']
    template_name = 'note.html'

    def get_success_url(self):
        view_name = 'mynotes'
        return reverse(view_name)


@login_required(login_url='/accounts/login/')
def mynotes(request):
    add_form = NoteForm()
    search_form = SearchForm()
    note_list = Note.objects.filter(author=request.user).order_by('created')

    data = {
        'search_form': search_form,
        'add_form': add_form,
        'note_list': note_list
    }

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            pass
            # search_data = json.load(request)
            # results = search_validator(note_list, search_data)
            # print(render_to_string('search_results.html', {'results': results}))
            # html = render_to_string('search_results.html', {'results': results})
            # return HttpResponse(html)
        if request.method == 'DELETE':
            note_id = json.load(request)['id']
            note = note_list.get(id=note_id)
            note.delete()
    if request.method == 'POST':
        note = Note()
        note.title = request.POST.get('title')
        note.text = request.POST.get('text')
        note.author = request.user
        note.save()
        return HttpResponseRedirect('/mynotes')
    return render(request, 'usernotes.html', context=data)
