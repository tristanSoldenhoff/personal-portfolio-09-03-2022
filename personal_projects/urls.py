from django.urls import path
from . import views

app_name = 'personal_projects'                                                               #app_name is a django variable that helps with all_blogs.html        <a href="{% url 'blog:detail' blog.id %}" ><h2>{{ blog.title }}</h2></a>

urlpatterns = [
    path('', views.all_projects, name='all_projects'),

]
