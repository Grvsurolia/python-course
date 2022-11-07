from django.shortcuts import render
from .models import *

def home(request):
    all_products = Product.objects.all()
    context = {"products":all_products}
    return render(request, "home.html", context)