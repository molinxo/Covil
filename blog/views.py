
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Project
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def blog(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'blog/blog.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def projects(request):
    projects = Project.objects.order_by('-created_at')
    return render(request, 'blog/projects.html', {'projects': projects})

def project_detail(request, pk):
    post = get_object_or_404(Project, pk=pk)
    return render(request, 'blog/project_detail.html', {'post': post})

def gear(request):
    return render(request, 'blog/gear.html')
