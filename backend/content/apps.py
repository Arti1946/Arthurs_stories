from django.apps import AppConfig


class ContentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "content"

    def ready(self):
        """Добавление signals.py."""
        try:
            import content.signals
        except ImportError:
            pass
