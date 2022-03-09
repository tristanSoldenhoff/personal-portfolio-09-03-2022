from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()                                            #grab all objects from the database that are project objects
    return render(request, 'main_site/index.html', {'projects':projects})        #refers and sends objects to html page
