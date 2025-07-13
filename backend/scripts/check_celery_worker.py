import sys
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quant.settings')

app = Celery('quant')
app.config_from_object('django.conf:settings', namespace='CELERY')

try:
    response = app.control.ping(timeout=2.0)
    if response:
        print(f'Celery worker is alive: {response}')
        sys.exit(0)
    else:
        print('No Celery workers responded.')
        sys.exit(1)
except Exception as e:
    print(f'Celery worker check failed: {e}')
    sys.exit(2) 