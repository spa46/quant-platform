import os

settings_env = os.environ.get('DJANGO_ENV', 'development')

if settings_env == 'production':
    from .settings.production import *
else:
    from .settings.development import *
