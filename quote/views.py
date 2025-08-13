from django.shortcuts import render, redirect
from django.views import generic
from .models import Note
from django import forms

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
        # Optional: set author if user is authenticated
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        # Optional: mark as not approved yet
        form.instance.approved = False
        return super().form_valid(form)
