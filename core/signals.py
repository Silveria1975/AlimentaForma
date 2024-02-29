from django.contrib.auth.models import Group
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver

from alimenta_forma.core.models import Profile


@receiver(post_save, sender=Profile)
def add_user_to_students_group(sender, instance, created, **kwargs):
    if created:
        group, created = Group.objects.get_or_create(name='estudiante')
        instance.user.groups.add(group)


def create_default_groups():
    Group.objects.get_or_create(name='estudiante')
    Group.objects.get_or_create(name='profesor')
    Group.objects.get_or_create(name='empresa')
    Group.objects.get_or_create(name='administrativo')


# Registrar la función de creación de grupos al iniciar la aplicación
@receiver(post_migrate, sender=None)
def create_groups_on_migrate(sender, **kwargs):
    create_default_groups()
