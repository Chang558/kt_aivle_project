from django.apps import AppConfig


class PracticeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game'

    def ready(self):
        import game.signals
