from django.shortcuts import render, get_object_or_404                          #get_object_or_404    is used for getting singular blogs
from .models import Blog

def all_blogs(request):
    #blogs = Blog.objects.order_by('-date')[:5]                                 limits the amount of blog post shown on thte page
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):                                                   #blog_id from urls.py
    blog = get_object_or_404(Blog, pk=blog_id)                                  #extract single blog......pk=primary key
    return render(request, 'blog/detail.html', {'blog':blog})                   #send blog to detail.html
