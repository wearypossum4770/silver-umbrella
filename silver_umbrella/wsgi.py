from os import environ

from django.core.wsgi import get_wsgi_application
from hypercorn.middleware import AsyncioWSGIMiddleware

environ.setdefault("DJANGO_SETTINGS_MODULE", "silver_umbrella.settings")
# wsgi_app = get_wsgi_application()
application = get_wsgi_application()  # AsyncioWSGIMiddleware(wsgi_app)
