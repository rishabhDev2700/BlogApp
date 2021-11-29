from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blogposts/', views.blogposts, name="blogposts"),
    path('blog/<int:pk>', views.blog, name="blog"),
    path('blog/publish/', views.publish_blog, name='create_blog'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]
