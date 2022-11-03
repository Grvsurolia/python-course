from django.shortcuts import redirect, render
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/profile/login/")
def Create_profile_view(request):
    if request.method == "POST":
        print("iffffffffffffffffff")
        post_data = request.POST
        # name = post_data["name"]
        # class_name = post_data["class"]
        # roll_no = post_data["roll_no"]
        # sub = post_data["subject"]

        profileOb = Profile(student_name = post_data["name"], class_name = post_data["class"], roll_no = post_data["roll_no"], subject = post_data["subject"])
        profileOb.save()
        messages.success(request, "Saved Successfully" )
        return redirect("/profile/create/")
    else:
        print("elseeeeeeeeeeeeeeeeee")
        return render(request, "create_profile.html")


@login_required(login_url="/profile/login/")
def Profile_view(request):
    all_profiles = Profile.objects.all()
    context = {"profiles":all_profiles}
    return render(request, "profile_table.html", context)


def register_view(request):
    if request.method == "POST":
        print("Register")
        post_data = request.POST
        name = post_data["name"]
        email = post_data["email"]
        password1 = post_data["password1"]
        password2 = post_data["password2"]

        if password1 != password2:
            messages.error(request, "Password Not Match")
        else:
            userOb = User.objects.create_user(username=name, email=email, password=password1)
            messages.success(request, "Saved Successfully")

        return redirect("/profile/register/")

    else:
        return render(request, "register.html")


def login_view(request):
    
    if request.method == "POST":
        post_data = request.POST
        user = authenticate(username=post_data["username"], password=post_data["password"])
        if user == None:
            messages.error(request, "Username or Password is incorrect")
            return redirect("/profile/login/")
        else:
            login(request, user)
            messages.info(request, "Logged in successfully")
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect("/profile/table/")

    else:
        return render(request, "login.html")

def logout_view(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/profile/login/")