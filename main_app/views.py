from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post, Student
from .forms import MessageForm



# ========= CBV's ===================

class PostCreate(CreateView):
  model = Post
  fields = '__all__'

class PostUpdate(UpdateView):
  model = Post
  fields = ['title', 'content', 'date']
  success_url = '/posts/'


class PostDelete(DeleteView):
  model = Post
  success_url = '/posts/'

# ========= Functions ===================

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def posts_index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', { 'posts': posts })

def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post' : post} )

def add_message(request, post_id):
  form = MessageForm(request.POST)
  if form.is_valid():
    new_message = form.save(commit=False)
    new_message.post_id = post_id
    new_message.save()
  return redirect('detail', post_id= post_id)



