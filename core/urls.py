from django.contrib import admin
from django.urls import path
from .views import HomeView, CoursesView, AnnouncementsView,  RegisterView, LoginView, logoutView, PasswordChangeView, ProfileView
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    # Pagina de inicio
    path('', HomeView.as_view(), name = 'home'),
    # Pagina de cursos
    path('courses/', CoursesView.as_view(), name = 'courses'),
    # Pagina de anuncios
    path('announcements/', AnnouncementsView.as_view(), name = 'announcements'),
    # Inicio de Sesión
    path('login/', LoginView.as_view(), name = 'login'),
    # Cierre de Sesión
    path('logout/', logoutView, name = 'logout'),
    # Registro de nuevo usuario
    path('register/', RegisterView.as_view(), name = 'register'),
    # Cambiar contraseña
    path('password_change/', PasswordChangeView.as_view(), name = 'password_change'), # Falta el enlace
    # Perfil de usuario
    path('profile/', ProfileView.as_view(), name = 'profile')
]