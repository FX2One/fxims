from django.apps import AppConfig


class CustomCmdConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_cmd'
