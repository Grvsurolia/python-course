from django.shortcuts import render
from .models import *

def home(request):
    all_categories = Category.objects.all()
    all_products = Product.objects.all()
    context = {"products":all_products, "categories":all_categories}
    return render(request, "home.html", context)


def Category_products(request, category_id):
    all_categories = Category.objects.all()
    categoryOb = Category.objects.get(id = category_id)
    products = Product.objects.filter(category = categoryOb)
    context = {"products":products, "categories":all_categories}
    return render(request, "category_product.html", context)

def single_product(request, product_id):
    all_categories = Category.objects.all()
    productOb = Product.objects.get(id=product_id)
    context = {"product":productOb,"categories":all_categories}
    return render(request, "single_product.html", context)