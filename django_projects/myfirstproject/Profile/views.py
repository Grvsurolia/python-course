from django.shortcuts import redirect, render
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User

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