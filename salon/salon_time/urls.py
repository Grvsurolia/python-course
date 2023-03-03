from django.urls import path
from .views import *

urlpatterns = [
    path('',available_time, name="available_time")
]