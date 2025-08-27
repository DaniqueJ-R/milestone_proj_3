"""App configuration for the quote application."""

from django.apps import AppConfig


class QuoteConfig(AppConfig):
    """Configuration class for the Quote app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "quote"
