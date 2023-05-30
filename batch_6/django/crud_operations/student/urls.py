from django.urls import path
from .views import Home, Details

urlpatterns = [
    path("home/", Home),
    path("details/", Details)
]