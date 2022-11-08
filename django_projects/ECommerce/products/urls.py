from django.urls import path 
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("category/<int:category_id>/",views.Category_products, name="category_products"),
    path("product/<int:product_id>/",views.single_product, name="single_product"),
]