from django.apps import AppConfig
from django.db import connection


class PerevalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pereval_app'
    verbose_name = 'Перевал'

    def ready(self):
        with connection.cursor() as cursor:
            cursor.execute('CREATE SEQUENCE IF NOT EXISTS pereval_id_seq')