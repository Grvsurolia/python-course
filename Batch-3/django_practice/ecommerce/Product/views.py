from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    context = {
        "all_products":all_products,
        "all_categories":all_categories,
    }
    return render(request, "index.html", context)


@login_required(login_url='/login')
def product_page(request, pk):
    product = Product.objects.get(id=pk)
    all_categories = Category.objects.all()
    context = {
        "product":product,
        "all_categories":all_categories,
    }
    return render(request, "product.html",context)


def loginView(request):
    if request.method == "POST":
        post_data = request.POST

        print(post_data)
        username = post_data["username"]
        password = post_data["password"]
        
        user = User.objects.filter(username=username)

        print("userrrrrrrr = ",user)

        if user.exists():
            print("Login")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                print("Please enter valid username or password")
                return redirect("/login")

        else:
            print("User not found")
            return redirect("/login")

    else:
        counter = []
        for i in range(0, 260):
            counter.append(i)
        context = {
            "counter":counter,
        }
        return render(request, "login.html",context)


def registerView(request):
    print(request.method)
    if request.method == "POST":
        post_data = request.POST
        print(post_data)
        
        full_name = post_data["full_name"]
        email = post_data["email"]
        username = post_data["username"]
        password1 = post_data["password1"]
        password2 = post_data["password2"]

        if password1 != password2:
            print("Password Not Matched")
            return redirect("/register")

        # user = User()
        # print(user)
        full_name_list = full_name.split(" ")
        # print(full_name_list)
        # user.first_name = full_name_list[0]
        # user.last_name = full_name_list[1]
        # user.email = email
        # user.username = username
        # user.password = password1

        # user.save()

        user = User.objects.create_user(first_name=full_name_list[0], last_name=full_name_list[1], email=email, username=username, password=password1)
        print("registered user = ",user, type(user))
        print("Saved Successfully")

        return redirect("/")


    else:
        counter = []
        for i in range(0, 260):
            counter.append(i)
        context = {
            "counter":counter,
        }
        return render(request, "register.html",context)