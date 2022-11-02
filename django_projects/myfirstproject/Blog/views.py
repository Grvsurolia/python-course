from django.shortcuts import redirect, render
from .models import Blog

def blog_view(request):
    all_blogs = Blog.objects.all()
    context = {"all_blogs":all_blogs}
    return render(request, "blog.html", context)


def create_blog_view(request):
    if request.method == "POST":
        # post_data = request.POST
        # print(post_data)
        # name = post_data["blog_name"]
        # content = post_data["content"]
        # blog_date = post_data["date"]
        # image = request.FILES["image"]
        # language = post_data["language"]

        # print(image)
        form = Blog(request.POST, request.FILES)
        # blog_ob = Blog(blog_name=name, blog_content=content, language=language, blog_date=blog_date)
        # if form.is_valid():
        form.save()

        return redirect("/blog")

    else:
        return render(request, "create_blog.html")


def update_blog_view(request, id):
    if request.method == "POST":
        post_data = request.POST
        blog_data = Blog.objects.get(id=id)
        blog_data.blog_name = post_data["blog_name"]
        blog_data.blog_content = post_data["content"]
        blog_date = post_data["date"]
        blog_data.language = post_data["language"]
        blog_data.save()
        return redirect("/blog")

    else:
        blog_data = Blog.objects.get(id=id)
        context = {"blog":blog_data}
        return render(request, "update_blog.html", context)


def delete_blog_view(request, id):
    blog_data = Blog.objects.get(id=id)
    blog_data.delete()
    return redirect("/blog")