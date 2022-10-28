from django.shortcuts import render
from .models import Blog

def blog_view(request):
    all_blogs = Blog.objects.all()
    context = {"all_blogs":all_blogs}
    return render(request, "blog.html", context)