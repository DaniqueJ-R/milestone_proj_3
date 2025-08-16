from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Model to store notes (quotes) created by users
class Note(models.Model):
    CATEGORY = (
        (0, "Uncategorized"),
        (1, "Stress"),
        (2, "Depression"),
        (3, "Anxiety"),
    )
    content = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default='anonymous', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    category = models.IntegerField(choices = CATEGORY, default=0, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='note'
    )

    class Meta:
        ordering = ["created_on"] # Order by creation date in ascending order

    def __str__(self):
        return f"quote-'{self.content}' by {self.name}"


# Background model to store theme and other settings
class Background(models.Model):
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
    audio = models.FileField(upload_to='audio/', blank=True, null=True)

    def __str__(self):
        return self.theme