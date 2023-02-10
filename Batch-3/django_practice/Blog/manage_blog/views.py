from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Blog, CustomUser
from django.contrib import messages


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
        blogOb = Blog(title=post_data["title"], content=post_data["content"], writer=user, image=request.FILES["image"])
        # blogOb.title = post_data["title"]
        # blogOb.content = post_data["content"]
        # blogOb.writer = user
        # blogOb.image = request.FILES["image"]
        print("New Blog = ",blogOb)
        blogOb.save()
        return redirect("/")
    else:
        all_users = CustomUser.objects.all().order_by("-id")
        context = {
            "all_users":all_users
        }
        return render(request, "create_blog.html", context)
    

def updateBlogView(request, pk):
    all_users = CustomUser.objects.all()
    blog_data = Blog.objects.get(id=pk)
    context = {
        "all_users":all_users,
        "blog_data":blog_data,
    }
    return render(request, "update_blog.html",context)


def SaveUpdatedBlogView(request, pk):
    print(request.method)
    if request.method == "POST":
        post_data = request.POST
        print(request.FILES)
        print(post_data)
        blog = Blog.objects.get(id = pk)
        user = CustomUser.objects.get(id = post_data["writer"])
        blog.title = post_data["title"]
        blog.content = post_data["content"]
        blog.image = request.FILES["image"]
        blog.writer = user

        blog.save()
        messages.success(request, "Updated Successfully" )
        return redirect("/update/"+str(pk)+"/")
    
