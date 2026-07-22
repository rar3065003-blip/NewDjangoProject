from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('blog:blog_list')

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('blog:blog_list')

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'  # Шаблон подтверждения удаления
    success_url = reverse_lazy('blog:blog_list')

# Create your views here.
