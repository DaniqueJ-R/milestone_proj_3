from django.contrib import admin
from .models import Note, Background
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):
    list_display = ("content", "author", "name", "status", "category", "created_on")
    list_filter = ("status", "created_on", "category")
    search_fields = ("content", "name")
    summernote_fields = ("content",)


# Register your models here.

admin.site.register(Background)
