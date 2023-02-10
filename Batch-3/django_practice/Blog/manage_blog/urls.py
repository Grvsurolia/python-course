from django.urls import path
from .views import BlogView, CreateBlogView, updateBlogView, SaveUpdatedBlogView

urlpatterns = [
    path("", BlogView, name="blog"),
    path("create/", CreateBlogView, name="create_blog"),
    path("update/<int:pk>/", updateBlogView, name="update_blog"),
    path("save_update/<int:pk>/", SaveUpdatedBlogView, name="save_updated_blog"),
]
