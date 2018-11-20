from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
import notifier.routing
from backend.consumers import UploadConsumer


application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(
            notifier.routing.websocket_urlpatterns,
            ),
        )
    ),
    "channel": ChannelNameRouter({
        "file-upload":  UploadConsumer,
    }),
})
