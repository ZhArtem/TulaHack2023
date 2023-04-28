# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post


class PostsHome(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_moderated=True)


class ShowPost(DetailView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'post'
