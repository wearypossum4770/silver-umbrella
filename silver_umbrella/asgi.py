import asyncio
import signal
from os import environ

import django
from django.core.asgi import get_asgi_application
from django.core.cache.backends.memcached import BaseMemcachedCache
from hypercorn.asyncio import serve
from hypercorn.config import Config
from hypercorn.middleware import DispatcherMiddleware

environ.setdefault("DJANGO_SETTINGS_MODULE", "mighty_meadow.settings")
BaseMemcachedCache.close = lambda self, **kwargs: None

shutdown_event = asyncio.Event()


def _signal_handler(*_):
    shutdown_event.set()


application = get_asgi_application()
