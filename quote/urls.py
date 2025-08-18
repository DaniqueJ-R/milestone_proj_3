from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Home
    path('', views.NotesList.as_view(), name='home'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.SignUpView.as_view(template_name='accounts/signup.html'), name='signup'),

    # Notes
    path('my-notes/', views.MyNotesView.as_view(), name='my_notes'),
    path('note/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='edit_note'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete_note'),
    path('notes-json/', views.NotesJson.as_view(), name='notes_json'),
    path('write-a-note/', views.WriteANoteView.as_view(), name='write_a_note'),
]

# Password reset
# path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
# path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
# path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
# path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
