from django.shortcuts import render
from django.views import generic
from .models import Note

# Create your views here.
class NotesList(generic.ListView):
    model = Note
    template_name = 'quote/home.html'
    context_object_name = 'notes_list'

    def get_queryset(self):
        return Note.objects.filter(approved=True).order_by('-created_on')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Take a Breath - Home"
        return context