from django.apps import AppConfig

# Define an AppConfig subclass to customize the application configuration
class MainConfig(AppConfig):
    # Set the default auto field for models in this app to BigAutoField
    default_auto_field = "django.db.models.BigAutoField"
    # Set the name of the app
    name = "main"
