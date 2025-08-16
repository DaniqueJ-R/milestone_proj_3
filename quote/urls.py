from . import views
from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('notes-json/', views.NotesJson.as_view(), name='notes-json'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='quote/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('write-note/', views.WriteANoteView.as_view(), name='write_note'),
    path('', views.NotesList.as_view(), name='home'),
]