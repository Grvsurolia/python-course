from django.urls import path 
from .views import *

urlpatterns = [
    path("home1/", home1),
    path("home2/", home2),
]

