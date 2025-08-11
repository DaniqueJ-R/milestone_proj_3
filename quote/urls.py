from . import views
from django.urls import path


urlpatterns = [
    path('', views.NotesList.as_view(), name='index'),
]