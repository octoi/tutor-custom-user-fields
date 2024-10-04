from django.apps import AppConfig

class CustomUserFieldsConfig(AppConfig):
    name = 'custom_user_fields'
    verbose_name = 'Custom User Fields'

    def ready(self):
        # Import the signals when the app is ready
        import custom_user_fields.signals
