from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Notes(models.Model):
    CATEGORY = (
        (0, "Uncategorized"),
        (1, "Stress"),
        (2, "Depression"),
        (3, "Anxiety"),
    )
    content = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default='anonymous')
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    category = models.IntegerField(choices = CATEGORY, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        ordering = ["created_on"] # Order by creation date in ascending order

    def __str__(self):
        return f"quote-'{self.content}' by {self.name}"


class Sticker(models.Model):
    sticker_type = models.ForeignKey('StickerTypeModel', on_delete=models.CASCADE)
    notes = models.ForeignKey(Notes, on_delete=models.CASCADE, related_name='stickers')
    x_position = models.IntegerField(default=0)
    y_position = models.IntegerField(default=0)
    rotation = models.FloatField(default=0.0)

    def __str__(self):
        return self.sticker_type


THEME_CHOICES = (
    (0, "Cosmic"),
    (1, "Ocean"),
    (2, "Forest"),
    (3, "Sunset"),
)

class StickerTypeModel(models.Model):
    sticker_name = models.CharField(max_length=100)
    image = models.FileField(upload_to='stickers/')
    category = models.IntegerField(choices=THEME_CHOICES, default='0')

    def __str__(self):
        return self.sticker_name


class Background(models.Model):
    theme = models.IntegerField(choices=THEME_CHOICES, default=0)
    background_colour = models.CharField(max_length=100)
    note_color = models.CharField(max_length=100)
    font = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)

    def __str__(self):
        return self.theme