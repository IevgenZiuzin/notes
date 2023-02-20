from django.shortcuts import render
from django.views import generic
from notes.models import *


class UserNotesListView(generic.ListView):
    model = Note
    ordering = ['created']
    template_name = 'usernotes.html'
    paginate_by = 10

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user).order_by('created')


class NoteDetail(generic.DetailView):
    model = Note
    template_name = 'note.html'


def index(request):
    return render(request, 'index.html')


