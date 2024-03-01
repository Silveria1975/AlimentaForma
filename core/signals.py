from django.contrib.auth.models import Group
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from .models import Profile, Registration

# Crea grupos por defecto luego de hacer las migraciones, si no existen
def create_default_groups():
    Group.objects.get_or_create(name='estudiante')
    Group.objects.get_or_create(name='profesor')
    Group.objects.get_or_create(name='empresa')
    Group.objects.get_or_create(name='administrativo')

# Registrar la función de creación de grupos al iniciar la aplicación
@receiver(post_migrate, sender=None)
def create_groups_on_migrate(sender, **kwargs):
    create_default_groups()

# Asigna el usuario creado al grupo estudiante
@receiver(post_save, sender=Profile)
def add_user_to_students_group(sender, instance, created, **kwargs):
    if created:
        group, created = Group.objects.get_or_create(name='estudiante')
        instance.user.groups.add(group)

# Crea un registro de notas para cada estudiante
@receiver(post_save, sender = Registration)
def create_marks (sender, instance, created, **kwargs):
    if created:
        Mark.objects.create(
            course = instance.course,
            student = instance.student,
            mark_1 = None,
            mark_2 = None,
            mark_3 = None,
            average = None,
        )
# VER SI SE VA A EMPLEAR UN SISTEMA DE ASISTENCIAS!!!!!!
# # Guarda las asistencias de un estudiante
# @receiver(post_save, sender = Registration)
# def save_attendance (sender, instance, created, **kwargs):
#     if created:
#         #crea un registro de clases por cada clase que tiene el curso (class_quantity)
#         for i in range (1, instance.course.class_quantity + 1):
#             Attendance.objects.create(
#                 course = instance.course,
#                 student = instance.student,
#                 date = None,
#                 present = None,
#             )