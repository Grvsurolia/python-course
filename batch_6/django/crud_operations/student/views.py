from django.shortcuts import render, redirect
from .models import StudentDetails

def Home(request):
    if request.method == "POST":
        print("Save data")
        print(request.POST)
        name = request.POST["name"]
        class_ = request.POST["class"]
        age = request.POST["age"]
        stu = StudentDetails.objects.create(name=name, class_=class_, age=age)
        return redirect('/student/home/')
    else:
        print("Elseeeeeeeeeeeeeeeeeeeeeeeeeee")
        return render(request, "home.html")
    

def Details(request):
    all_students = StudentDetails.objects.all()
    context = {
        "all_students":all_students
    }
    return render(request, "details.html", context)