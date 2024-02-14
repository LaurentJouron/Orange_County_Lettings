from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the profiles app.

    Explanation:
        This class represents the configuration for the profiles app.
        It specifies the default auto field and the name of the app.

    Examples:
        >>> config = ProfilesConfig()
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"
