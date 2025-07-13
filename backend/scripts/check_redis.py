import redis
import os
import sys

# Try to get the broker URL from Django settings or use default
broker_url = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')

try:
    r = redis.Redis.from_url(broker_url)
    pong = r.ping()
    if pong:
        print('Redis is alive!')
        sys.exit(0)
    else:
        print('Redis did not respond to ping.')
        sys.exit(1)
except Exception as e:
    print(f'Redis connection failed: {e}')
    sys.exit(2) 