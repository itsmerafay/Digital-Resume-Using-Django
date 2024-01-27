from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    # Now when the app is running the signals too will work
    def ready(self):
        import main.signals

