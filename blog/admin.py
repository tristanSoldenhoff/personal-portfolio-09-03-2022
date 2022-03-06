from django.contrib import admin
from .models import Blog

# THIS FILE IF FOR ALLOWING WHICH MODELS SHOW ON THE ADMIN SITE

admin.site.register(Blog)    #import class Blog() from models.py and shows it on admin site
