from django.urls import path
from app.views import chatbot

urlpatterns = [
    path('chatbot/', chatbot, name='chatbot'),
]
