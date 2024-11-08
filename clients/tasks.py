# clients/tasks.py
from celery import shared_task
from django.db import connection
from celery import Celery
from celery.schedules import crontab

app = Celery()

@shared_task
def refresh_materialized_view():
    with connection.cursor() as cursor:
        cursor.execute('REFRESH MATERIALIZED VIEW client_summary;')

# Schedule this task every day at midnight
app.conf.beat_schedule = {
    'refresh-client-summary-view': {
        'task': 'clients.tasks.refresh_materialized_view',
        'schedule': crontab(hour=0, minute=0),
    },
}
