"""Models for handling notes, bad words, and background themes in the app."""

from django.db import models
from django.contrib.auth.models import User


def get_removed_user():
    """Return the 'Removed' user, creating it if necessary."""
    user, created = User.objects.get_or_create(
        username="Removed",
        defaults={
            "email": "removed@example.com",
            "password": "",
        },
    )
    return user


class Note(models.Model):
    """Model to store notes (quotes) created by users."""

    CATEGORY = (
        (0, "Uncategorized"),
        (1, "Stress"),
        (2, "Depression"),
        (3, "Anxiety"),
    )

    STATUS = (
        (0, "Pending"),
        (1, "Approved"),
        (2, "Denied"),
    )

    content = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default="anonymous", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.IntegerField(choices=CATEGORY, default=0, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET(get_removed_user),
        related_name="notes",
    )

    class Meta:
        """Metadata for ordering notes by creation date."""

        ordering = ["created_on"]

    def __str__(self):
        """Return a string representation of the note."""
        return f"quote-'{self.content}' by {self.name}"


class BadWord(models.Model):
    """Model to store banned words."""

    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """Return the word as its string representation."""
        return self.word


class Background(models.Model):
    """Model to store theme and background settings."""

    THEME_CHOICES = (
        (0, "Cosmic"),
        (1, "Ocean"),
        (2, "Forest"),
        (3, "Sunset"),
    )

    theme = models.IntegerField(choices=THEME_CHOICES, default=0)
    background_colour = models.CharField(max_length=100)
    note_color = models.CharField(max_length=100)
    font = models.CharField(max_length=100)
    audio = models.FileField(upload_to="audio/", blank=True, null=True)

    def __str__(self):
        """Return the theme as its string representation."""
        return str(self.theme)
