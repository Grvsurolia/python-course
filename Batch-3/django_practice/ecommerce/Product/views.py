from django.shortcuts import render, redirect
from .models import Product, Category

def index(request):
    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    context = {
        "all_products":all_products,
        "all_categories":all_categories,
    }
    return render(request, "index.html", context)


def product_page(request, pk):
    product = Product.objects.get(id=pk)
    all_categories = Category.objects.all()
    context = {
        "product":product,
        "all_categories":all_categories,
    }
    return render(request, "product.html",context)