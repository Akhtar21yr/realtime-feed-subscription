"""
ASGI config for realtime_feed_subscription project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from feeds.routings import websocket_urlpatterns
# from channels.auth import 
from feeds.jwt_middleware import jwt_auth_middleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realtime_feed_subscription.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": jwt_auth_middleware(
            URLRouter(websocket_urlpatterns) 
        )
    }
)
