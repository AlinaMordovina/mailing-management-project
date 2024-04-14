from time import sleep

from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailing"

    # def ready(self):
    #     from django.core.management import call_command
    #     sleep(2)
    #
    #     call_command('runapscheduler')
