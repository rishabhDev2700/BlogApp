import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from BlogPosts.forms import BlogForm
from BlogPosts.models import Blog


def home(request):
    recent_blog = Blog.objects.filter(pub_date__month__gte=datetime.date.today().month)
    blogs = Blog.objects.all()
    context = {'blogs': blogs, 'recent_blog': recent_blog}
    return render(request, 'blog/home.html', context)


def blog(request, pk):
    full_blog = Blog.objects.get(pk=pk)
    context = {'blog': full_blog}
    return render(request, 'blog/blog.html', context)


def contact(request):
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, 'blog/about.html')


def blogposts(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})


def publish_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=Blog(author=request.user, pub_date=datetime.date.today()))
        if form.is_valid():
            form.save()
            return redirect('blogposts')
        else:
            return HttpResponse("Error Occurred")
    form = BlogForm()
    return render(request, 'blog/blog_form.html', {'form': form})


def profile(request):
    return render(request, 'blog/profile.html')
