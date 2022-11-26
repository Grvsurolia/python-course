from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q



@login_required(login_url="/login/")
def home(request):
    all_categories = Category.objects.all()
    all_products = Product.objects.all()
    context = {"products":all_products, "categories":all_categories}
    return render(request, "home.html", context)


@login_required(login_url="/login/")
def Category_products(request, category_id):
    all_categories = Category.objects.all()
    categoryOb = Category.objects.get(id = category_id)
    products = Product.objects.filter(category = categoryOb)
    context = {"products":products, "categories":all_categories}
    return render(request, "category_product.html", context)


@login_required(login_url="/login/")
def single_product(request, product_id):
    all_categories = Category.objects.all()
    productOb = Product.objects.get(id=product_id)
    context = {"product":productOb,"categories":all_categories}
    return render(request, "single_product.html", context)


def register_view(request):
    if request.method == "POST":
        print("Register")
        post_data = request.POST
        print(post_data)
        name = post_data["name"]
        email = post_data["email"]
        password1 = post_data["password1"]
        password2 = post_data["password2"]

        if password1 != password2:
            messages.error(request, "Password Not Match")
        else:
            userOb = User.objects.create_user(username=name, email=email, password=password1)
            messages.success(request, "Saved Successfully")
        return redirect("/register/")

    else:
        return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        print("login")
        post_data = request.POST
        user = authenticate(username=post_data["username"], password=post_data["password"])
        if user == None:
            messages.error(request, "Username or Password is incorrect")
            return redirect("/login/")
        else:
            login(request, user)
            messages.info(request, "Logged in successfully")
            return redirect("/")

    else:
        return render(request, "login.html")


def logout_view(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/login/")


def search_view(request):
    print("Searchhhhhhhhh ho raha h........")
    search_query = request.GET["search"]

    products = Product.objects.filter(Q(name__icontains = search_query) | Q(description__icontains = search_query) | Q(price__icontains = search_query))
    all_categories = Category.objects.all()

    context = {"products": products, "categories":all_categories}

    return render(request, "home.html", context)