import os
import sys

pidfile = 'celerybeat.pid'
if not os.path.exists(pidfile):
    print("Celery Beat PID file not found. Beat may not be running.")
    sys.exit(1)

with open(pidfile) as f:
    pid = int(f.read().strip())

try:
    os.kill(pid, 0)
    print(f"Celery Beat is running with PID {pid}.")
    sys.exit(0)
except OSError:
    print(f"Celery Beat process with PID {pid} not found.")
    sys.exit(2) 