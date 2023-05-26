import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

app = Celery('delivery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.timezone = 'UTC'


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


# Periodical tasks, based in delivery/tasks.py. Car's location updating every 3 minutes.
app.conf.beat_schedule = {
    'Update delivery cars locations': {
        'task': 'update_delivery_cars_locations',
        'schedule': 180,
    },
}
