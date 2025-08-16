from django import forms
from .models import Note

# Create your views here.

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
    