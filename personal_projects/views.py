from django.shortcuts import render, get_object_or_404                          #get_object_or_404    is used for getting singular blogs
from .models import Project

def all_projects(request):
    #blogs = Blog.objects.order_by('-date')[:5]                                 limits the amount of blog post shown on thte page
    projects = Project.objects.all()
    return render(request, 'personal_projects/all_projects.html', {'projects':projects})
