from django.contrib import admin
from .models import User, Course, Announcement, Registration, Mark, Suscription


# Registro de usuarios
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')
    list_filter = ('is_staff', 'email', 'username')
admin.site.register(User, UserAdmin)

# Registro de perfil
class CourseAdmin (admin.ModelAdmin):
    list_display = ('name', 'description', 'class_quantity', 'status')
    list_filter = ('name', 'status')
admin.site.register(Course, CourseAdmin)

# Registro de anuncios    
class AnnouncementAdmin (admin.ModelAdmin):
    list_display = ('name', 'description', 'status')
    list_filter = ('name', 'status')
admin.site.register(Announcement, AnnouncementAdmin)

# Registro de inscripciones
class RegistrationAdmin (admin.ModelAdmin):
    list_display = ('course', 'student', 'enabled')
    list_filter = ('course', 'student', 'enabled')
admin.site.register(Registration, RegistrationAdmin)

# Registro de calificaciones
class MarksAdmin (admin.ModelAdmin):
    list_display = ('course', 'student', 'mark_1', 'mark_2', 'mark_3', 'average')
    list_filter = ('course',)
admin.site.register(Mark, MarksAdmin)

# Registro de suscripción
class SuscriptionAdmin (admin.ModelAdmin):
    list_display = ('student', 'date', 'payment')
    List_filter = ('student', 'date')
admin.site.register(Suscription, SuscriptionAdmin)

