from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Blog

class HomePageView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"
    context_object_name = 'blog'
