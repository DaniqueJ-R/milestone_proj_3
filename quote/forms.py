"""Forms for handling notes and user signup in the application."""

from django import forms
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NoteForm(forms.ModelForm):
    """Form for creating and validating Note objects."""

    class Meta:
        """Metadata for NoteForm linking it to the Note model."""

        model = Note
        fields = ["content", "name", "category"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Write your quote here...",
                }
            ),
            "name": forms.TextInput(attrs={"placeholder": "Anonymous"}),
            "category": forms.Select(),
        }

    def clean_name(self):
        """Ensure a name is always set, defaulting to 'anonymous'."""
        name = self.cleaned_data.get("name")
        if not name:
            return "anonymous"
        return name

    def clean_category(self):
        """Ensure a category is always set, defaulting to 0 (Uncategorized)."""
        category = self.cleaned_data.get("category")
        if category is None:
            return 0  # Default to "Uncategorized"
        return category


class SignUpForm(UserCreationForm):
    """Form for handling user sign-up with an additional email field."""

    email = forms.EmailField(required=True)

    class Meta:
        """Metadata for SignUpForm linking it to the User model."""

        model = User
        fields = ("username", "email", "password1", "password2")
