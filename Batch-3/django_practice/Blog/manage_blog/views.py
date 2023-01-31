from django.shortcuts import render
# from django.http import HttpResponse
from .models import Blog


# def BlogView(request):
    # return HttpResponse("<h1>Welcome To My Blog</h1>")


def BlogView(request):
    all_blogs = Blog.objects.all()
    context = {
        "all_blogs":all_blogs,
    }
    return render(request, "blog.html", context)
