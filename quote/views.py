import json
import os

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .forms import NoteForm, SignUpForm
from .models import Note, BadWord


# Create your views here.


# This view handles user signup
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = reverse_lazy("home")  # redirect after signup

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # log in immediately after signup
        return response


# This view handles the home page displaying a list of notes
class NotesList(ListView):
    model = Note
    template_name = "quote/home.html"
    context_object_name = "notes_list"

    def get_queryset(self):
        return Note.objects.filter(status=1).order_by(
            "?"
        )  # Random order for the home page


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["notes"] = self.get_queryset().order_by("-created_on")
    return context


# This view handles the display of a single note for the home page
class NotesJson(View):
    def get(self, request):
        notes = Note.objects.filter(status=1).order_by("-created_on")
        data = [
            {
                "content": note.content,
                "name": note.name,
                "created_on": note.created_on.isoformat(),
            }
            for note in notes
        ]
        return JsonResponse(data, safe=False)


# This view handles the form submission for writing a new note
class WriteANoteView(LoginRequiredMixin, CreateView):
    form_class = NoteForm
    template_name = "quote/write-a-note.html"

    # Load badwords from database.
    def get_badwords(self):
        """Load badwords from database."""
        file_path = os.path.join(
            settings.BASE_DIR, "quote", "fixtures", "badwords.json"
        )
        with open(file_path, "r", encoding="utf-8") as f:
            badwords_data = json.load(f)
        # Extract words from JSON structure
        return [entry["fields"]["word"] for entry in badwords_data]

    def form_valid(self, form):
        # Assign author
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        else:
            form.instance.author = get_removed_user()

        # Set default name
        if not form.cleaned_data.get("name"):
            form.instance.name = "Anonymous"

        # Load banned words from database
        banned_words = self.get_badwords()
        content_lower = form.cleaned_data["content"].lower()

        if not content_lower.strip():
            return JsonResponse({"error": "Content cannot be empty."}, status=400)

        if any(bad_word in content_lower for bad_word in banned_words):
            form.instance.status = 0  # Pending
            message = "Your quote requires manual approval."
        else:
            form.instance.status = 1  # Approved
            message = "Your quote was submitted successfully!"

        self.object = form.save()

        return JsonResponse(
            {
                "quote": self.object.content,
                "name": self.object.name,
                "category": self.object.category,
                "category_display": self.object.get_category_display(),
                "message": message,
                "status": self.object.status,
            }
        )


# List of user’s notes
class MyNotesView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "quote/my-notes.html"
    context_object_name = "notes"
    pending_notes = Note.objects.filter(status=0).order_by("created_on")

    def get_queryset(self):
        # Only show the notes created by the logged-in user
        return Note.objects.filter(author=self.request.user)


# Update a note
class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "quote/edit-note.html"

    def get_queryset(self):
        # Prevent editing other people's notes
        return Note.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("my_notes")


# Delete a note
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "quote/delete-note.html"

    def get_queryset(self):
        # Prevent deleting other people's notes
        return Note.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("my_notes")
