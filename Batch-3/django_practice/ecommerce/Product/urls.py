from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="home"),
    path("product/<int:pk>/", views.product_page, name="product_page"),
    path("login/", views.loginView, name="login"),
    path("register/", views.registerView, name="register"),
    path("cart/", views.cartView, name="cart"),
    path("logout/", views.logoutView, name="logout"),
    path("add_to_cart/<int:product_id>/", views.add_to_cartView, name="add_to_cart"),
    path("delete_product_from_cart/<int:cart_id>/", views.delete_product_from_cartView, name="delete_product_from_cart"),
    path("category/<int:categ_id>/", views.category_productsView, name="category_product"),

]