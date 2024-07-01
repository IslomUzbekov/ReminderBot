
from django.urls import path

from .views import handle_message

urlpatterns = [
    path('webhook/', handle_message, name='handle_message')
]
