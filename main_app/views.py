from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView, DetailView


from .models import Post, Student, Message
from .forms import MessageForm, StudentForm



# ========= CBV's ===================

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/posts/'

    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

# class MessageCreate(CreateView):
#     model = Message
#     fields = ['title', 'content']
#     def form_valid(self, form):
#     # Assign the logged in user (self.request.user)
#         form.instance.student = self.request.user  # form.instance is the cat
#         # Let the CreateView do its job as usual
#         return super().form_valid(form)



class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/posts/'


class PostDelete(DeleteView):
    model = Post
    success_url = '/posts/'


class MessageDetail(DetailView):
    model = Message


class MessageUpdate(UpdateView):
    model = Message
    fields = ['comment']

    def get_success_url(self):
        return reverse('detail', kwargs={'post_id': self.object.post.id})


class MessageDelete(DeleteView):
    model = Message
    
    def get_success_url(self):
        return reverse('detail', kwargs={'post_id': self.object.post.id})

# ========= Functions ===================


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    message_form = MessageForm()
    return render(request, 'posts/detail.html', {'post': post, 'message_form': message_form})


# def message_details(request, post_id, message_id):
#     post = Post.objects.get(id=post_id)
#     message = Message.objects.get(id=message_id)
#     return render(request, 'yourtemplate', {'post': post, 'message': message})


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
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

