from django.urls import path
from . import consumers


ws_urlpatterns = [
    path('ws/notify', consumers.WSConsumer.as_asgi())
]