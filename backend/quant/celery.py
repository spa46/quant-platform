import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quant.settings')

app = Celery('quant')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks() 