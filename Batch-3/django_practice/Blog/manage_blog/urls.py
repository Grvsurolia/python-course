from django.urls import path
from .views import BlogView, CreateBlogView

urlpatterns = [
    path("", BlogView, name="blog"),
    path("create/", CreateBlogView, name="create_blog"),
]
