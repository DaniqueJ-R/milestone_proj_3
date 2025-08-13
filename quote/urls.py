from . import views
from django.urls import path



urlpatterns = [
    path('write-note/', views.WriteANoteView.as_view(), name='write_note'),
    path('', views.NotesList.as_view(), name='home'),
]