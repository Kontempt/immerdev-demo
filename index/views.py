# from django.shortcuts import render
from django.views import generic
from .models import Portfolio, Blog

class IndexView(generic.ListView):
    '''Returns index with corresponding model val.s'''
    template_name = 'index/main.html'
    context_object_name = 'index_list'
    queryset = Portfolio.objects.all()

class DetailView(generic.DetailView):
    '''returns details for a specific selected project'''
    model = Portfolio
    template_name = 'index/project.html'

class BlogView(generic.ListView):
    '''Returns blog with corresponding model val.s'''
    template_name = 'index/blog_main.html'
    context_object_name = 'blog_list'
    queryset = Blog.objects.all()
