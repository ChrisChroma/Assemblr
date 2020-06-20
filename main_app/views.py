from django.shortcuts import render, redirect

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def posts_index(request):
  posts = Cat.objects.all()
  return render(request, 'posts/index.html', { 'posts': posts })