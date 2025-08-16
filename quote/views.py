from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views import generic
from django.http import JsonResponse
from .models import Note
from django.views import View
from .forms import NoteForm

# Create your views here.

# This view handles the home page displaying a list of notes
class NotesList(generic.ListView):
    model = Note
    template_name = 'quote/home.html'
    context_object_name = 'notes_list'

    def get_queryset(self):
        return Note.objects.filter(approved=True).order_by('?') # Random order for the home page
    
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['notes'] = self.get_queryset().order_by('-created_on')
    return context

# This view handles the display of a single note
class NotesJson(View):
    def get(self, request):
        notes = Note.objects.filter(approved=True).order_by('-created_on')
        data = [
            {
                "content": note.content,
                "name": note.name,
                "created_on": note.created_on.isoformat()
            }
            for note in notes
        ]
        return JsonResponse(data, safe=False)

# This view handles the form submission for writing a new note
class WriteANoteView(CreateView):
    form_class = NoteForm
    template_name = 'quote/write-a-note.html'

    def form_valid(self, form):
        # Banned words check
        banned_words = ["badword1", "badword2", "badword3"]
        content_lower = form.cleaned_data['content'].lower()

        if not content_lower.strip():
            return JsonResponse({'error': 'Content cannot be empty.'}, status=400)

        if any(bad_word in content_lower for bad_word in banned_words):
            form.instance.approved = False
            message = "Your quote requires manual approval."
        else:
            form.instance.approved = True
            message = "Your quote was submitted successfully!"

        # Set default name if blank
        if not form.cleaned_data.get('name'):
            form.instance.name = "Anonymous"

        self.object = form.save()

        # Return JSON response for AJAX
        return JsonResponse({
            'quote': self.object.content,
            'name': self.object.name,
            'category': self.object.category,
            'category_display': self.object.get_category_display(),
            'message': message,
            'approved': self.object.approved        
        })

    def form_invalid(self, form):
        # Return form errors as JSON
        return JsonResponse({'errors': form.errors}, status=400)