from django.shortcuts import render, redirect
from django.views import generic
from .models import Note
from django import forms

# Create your views here.
# This view handles the home page displaying a list of notes
class NotesList(generic.ListView):
    model = Note
    template_name = 'quote/home.html'
    context_object_name = 'notes_list'

    def get_queryset(self):
        return Note.objects.filter(approved=True).order_by('?') # Random order for the home page


# This view handles the creation of a new note    
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content', 'name', 'category']
        widgets = {
            'content': forms.Textarea(attrs={'rows':3, 'placeholder': 'Write your quote here...'}),
            'name': forms.TextInput(attrs={'placeholder': 'Your name (if you want)'}),
            'category': forms.Select(),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            return 'anonymous'
        return name
    
    def clean_category(self):
        category = self.cleaned_data.get('category')
        if category is None:
            return 0 # Default to "Uncategorized"
        return category
    
# This view handles the form submission for writing a new note
class WriteANoteView(generic.CreateView):
    form_class = NoteForm
    template_name = 'quote/write-a-note.html'
    success_url = '/'

    def form_valid(self, form):
        # List of banned words (lowercase for easier matching)
        banned_words = ["badword1", "badword2", "badword3"]

        # Convert content to lowercase for checking
        content_lower = form.cleaned_data['content'].lower()
        # Check if the content is empty
        if not content_lower.strip():
            form.add_error('content', 'Content cannot be empty.')
            return self.form_invalid(form)
        # Check for banned words
        if any(bad_word in content_lower for bad_word in banned_words):
            form.instance.approved = False
            messages.warning(
                self.request,
                "Your quote contains language that requires manual approval before it appears."
            )
        else:
            form.instance.approved = True
            messages.success(
                self.request,
                "Your quote was submitted successfully and is now live!"
            )

        return super().form_valid(form)