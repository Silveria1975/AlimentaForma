from django.contrib import admin
from django.urls import path
from .views import HomeView, CoursesView, AnnouncementsView, CustomLoginView, RegisterView

urlpatterns = [
    # Pagina de inicio
    path('', HomeView.as_view(), name = 'home'),
    # Pagina de cursos
    path('courses/', CoursesView.as_view(), name = 'courses'),
    # Pagina de anuncios
    path('announcements/', AnnouncementsView.as_view(), name = 'announcements'),
    # Inicio de Sesión
    path('login/', CustomLoginView.as_view(), name = 'login'),
    # Registro de nuevo usuario
    path('register/', RegisterView.as_view(), name= 'register'),
]
