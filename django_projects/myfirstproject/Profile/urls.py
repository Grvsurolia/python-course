from django.urls import path
from .views import *

urlpatterns = [
    path("create/", Create_profile_view, name="create_profile"),
    path("table/", Profile_view, name="profile_table"),
    path("register/", register_view, name="register"),
]