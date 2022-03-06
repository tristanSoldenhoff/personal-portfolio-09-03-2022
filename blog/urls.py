from django.urls import path
from . import views

app_name = 'blog'                                                               #app_name is a django variable that helps with all_blogs.html        <a href="{% url 'blog:detail' blog.id %}" ><h2>{{ blog.title }}</h2></a>

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),                        #blog_id for numbered blog to show up on its own.
                                                                                #send blog_id to views.detail
]
