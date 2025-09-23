from django.apps import AppConfig

class StudyportalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "StudyPortal"

    def ready(self):
        import StudyPortal.dashboard  

