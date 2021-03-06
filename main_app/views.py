from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Student, Message
from .forms import MessageForm, StudentForm



# ========= CBV's ===================

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/posts/'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'


class MessageDetail(LoginRequiredMixin, DetailView):
    model = Message


class MessageUpdate(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ['comment']

    def get_success_url(self):
        return reverse('detail', kwargs={'post_id': self.object.post.id})


class MessageDelete(LoginRequiredMixin, DeleteView):
    model = Message
    
    def get_success_url(self):
        return reverse('detail', kwargs={'post_id': self.object.post.id})

# ========= Functions ===================

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

@login_required
def my_posts(request):
    my_posts = Post.objects.filter(user=request.user)
    return render(request, 'posts/my_posts.html', {'my_posts' : my_posts})

@login_required
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    message_form = MessageForm()
    return render(request, 'posts/detail.html', {'post': post, 'message_form': message_form})

@login_required
def add_message(request, post_id):
    form = MessageForm(request.POST)
    if form.is_valid():
        new_message = form.save(commit=False)
        new_message.post_id = post_id
        new_message.user = request.user
        new_message.save()
    return redirect('detail', post_id=post_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

