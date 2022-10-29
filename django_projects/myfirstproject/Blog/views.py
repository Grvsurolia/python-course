from django.shortcuts import redirect, render
from .models import Blog

def blog_view(request):
    all_blogs = Blog.objects.all()
    context = {"all_blogs":all_blogs}
    return render(request, "blog.html", context)


def create_blog_view(request):
    if request.method == "POST":
        post_data = request.POST
        name = post_data["blog_name"]
        content = post_data["content"]
        # image = post_data["image"]
        language = post_data["language"]

        blog_ob = Blog(blog_name=name, blog_content=content, language=language, blog_date="2022-10-29")
        blog_ob.save()

        return redirect("/blog")

    else:
        return render(request, "create_blog.html")