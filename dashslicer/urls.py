from .views import dash
from django.urls import path

urlpatterns = [
    path('', dash),
]