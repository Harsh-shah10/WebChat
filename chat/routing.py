from django.urls import path
from . import consumers

ASGI_urlpatterns = [
    path('wsocket1/<int:id>', consumers.ChatConsumer.as_asgi())
]
