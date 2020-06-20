from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post, Student, Message



# Create your views here.

class PostCreate(CreateView):
  model = Post
  fields = ['title', 'content', 'date']

class PostUpdate(UpdateView):
  model = Post
  fields = ['title', 'content', 'date']

class PostDelete(DeleteView):
  model = Post
  success_url = '/posts/'


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def posts_index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', { 'posts': posts })

def posts_detail(request):
    post = Post.objects.get(request, post_id)
    return render(request, 'posts/detail.html')