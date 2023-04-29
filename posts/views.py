from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post


def about(request):
    return render(request, 'posts/about.html')


class PostList(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_moderated=True)


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    pass

