import asyncio
import signal
from os import environ

import django
from django.core.asgi import get_asgi_application
from django.core.cache.backends.memcached import BaseMemcachedCache
from dotenv import find_dotenv, load_dotenv
from hypercorn.asyncio import serve
from hypercorn.config import Config
from hypercorn.middleware import DispatcherMiddleware
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

# import chat.routing

load_dotenv(find_dotenv())
environ.setdefault("DJANGO_SETTINGS_MODULE", "silver_umbrella.settings")
BaseMemcachedCache.close = lambda self, **kwargs: None

shutdown_event = asyncio.Event()


def _signal_handler(*_):
    shutdown_event.set()


application = get_asgi_application()
# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns)),
#     }
# )