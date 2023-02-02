from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Blog, CustomUser


# def BlogView(request):
    # return HttpResponse("<h1>Welcome To My Blog</h1>")


def BlogView(request):
    all_blogs = Blog.objects.all().order_by("-id")
    d = {
        "blogs":all_blogs,
    }
    return render(request, "blog.html", d)


def CreateBlogView(request):
    if request.method=="POST":
        post_data = request.POST
        user = CustomUser.objects.get(id=post_data["writer"])
        blogOb = Blog()
        blogOb.title = post_data["title"]
        blogOb.content = post_data["content"]
        blogOb.writer = user
        blogOb.save()
        return redirect("/blog/")
    else:
        all_users = CustomUser.objects.all().order_by("-id")
        context = {
            "all_users":all_users
        }
        return render(request, "create_blog.html", context)