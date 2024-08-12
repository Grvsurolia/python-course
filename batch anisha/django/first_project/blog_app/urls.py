from django.urls import path
from .views import *

urlpatterns = [
    path("", show_blog, name="show_blog"),
    path("create/", create_blog, name="create_blog"),
    path("save_blog/", save_blog, name="save_blog"),
    path("update_blog/<int:id>/", update_blog, name="update_blog"),
    path("delete_blog/<int:pk>/", delete_blog, name="delete_blog"),
    path("search/", search_blog, name="search_blog")
]