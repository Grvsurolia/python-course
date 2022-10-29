from django.urls import path
from .views import blog_view, create_blog_view

urlpatterns = [
    path("", blog_view, name="blog"),
    path("create/", create_blog_view, name="create_blog"),
]