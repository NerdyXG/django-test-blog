from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Blog

class HomePageView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

class CreateNewBlogView(CreateView):
    model = Blog
    template_name = 'new_blog.html'
    fields = [
        'title',
        'author',
        'body'
    ]
    success_url = '/'

class UpdateBlogView(UpdateView):
    model = Blog
    template_name = 'update_blog.html'
    fields = [
        'title',
        'body'
    ]

class DeleteBlogView(DeleteView):
    model = Blog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')
