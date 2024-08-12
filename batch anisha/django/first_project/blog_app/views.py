from django.shortcuts import render, redirect
from .models import Blog_data
from django.db.models import Q
from django.contrib import messages

def show_blog(request):
    # print("In Show blog")
    all_blogs = Blog_data.objects.all().order_by("-id")
    # print("all_blogs = ",all_blogs)
    return render(request, "blog.html", context={"all_blogs":all_blogs})

def create_blog(request):
    return render(request, "create_blog.html")

def save_blog(request):
    print("*****************In save blog.")
    post_data = request.POST
    html_title = post_data["html_title"]
    html_writer = post_data["html_writer"]
    html_content = post_data["html_content"]
    if len(html_title)>10:
        print("Max length")
        messages.error(request, 'Max length for title is 10 char.')
        if len(html_writer)>10:
            print("Max length")
            messages.error(request, 'Max length for writer is 10 char.')
            return redirect('/blog')
        return redirect('/blog')
    
    blogOb = Blog_data(title=html_title, writer=html_writer, content=html_content)
    blogOb.save()
    print("Blog created.................")
    return redirect('/blog')

def update_blog(request, id):
    if request.method=="POST":
        print("Update")
        post_data = request.POST
        html_title = post_data["html_title"]
        html_writer = post_data["html_writer"]
        html_content = post_data["html_content"]

        blogOb = Blog_data.objects.get(id=id)
        blogOb.title = html_title
        blogOb.writer = html_writer
        blogOb.content = html_content
        
        blogOb.save()
        return redirect("/blog")
    else:
        blogOb = Blog_data.objects.get(id=id)
        return render(request, "update_blog.html", context={"blog":blogOb})
    

def delete_blog(request, pk):
    blogOb = Blog_data.objects.get(id=pk)
    blogOb.delete()
    return redirect("/blog")


def search_blog(request):
    query = request.GET["query"]
    searched_blogs = Blog_data.objects.filter(Q(title__icontains = query) | Q(writer__icontains = query))
    return render(request, "blog.html", context={"all_blogs":searched_blogs})