from django.urls import path
from .consumers import MySyncConsumer

websocket_urlpatterns = [
    path('ws/sc/<str:groupkanaam>/', MySyncConsumer.as_asgi()),
]