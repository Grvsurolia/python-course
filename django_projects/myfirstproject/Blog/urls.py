from django.urls import path
from .views import *

urlpatterns = [
    path("", blog_view, name="blog"),
    path("create/", create_blog_view, name="create_blog"),
    path("update/<int:id>/", update_blog_view, name="update_blog"),
    path("delete/<int:id>/", delete_blog_view, name="delete_blog"),
]