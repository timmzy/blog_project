from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog

# Create your views here.


class Home(ListView):
    template_name = 'index.html'
    model = Blog


class BlogView(DetailView):
    template_name = 'blog-post.html'
    model = Blog