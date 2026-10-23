import os
from django.core.wsgi import get_wsgi_application

# Production default; override with DJANGO_SETTINGS_MODULE locally.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")
application = get_wsgi_application()
