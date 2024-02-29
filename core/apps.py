from django.apps import AppConfig
from django.contrib.auth import models as auth_models


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        # Registrar el modelo `Profile` con el administrador de usuarios
        auth_models.User.meta.get_field('profile').related_model = 'core.Profile'
