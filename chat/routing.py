from django.urls import path
from . import consumers

ASGI_urlpatterns = [
    path('wsocket1', consumers.ChatConsumer.as_asgi())
]
