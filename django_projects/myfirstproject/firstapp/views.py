from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home1(request):
    t = datetime.datetime.now()
    return HttpResponse("<h1 style='color:blue;'>Gaurav surolia " + str(t) + "</h1>")


def home2(request):
    context = {"name":"komal", "class":12, "roll_no":20}
    return render(request, "home.html", context)