from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin



from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
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


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'posts/add.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True


def contact(request):
    return HttpResponse("Обратная связь")


class RegisterUser(CreateView):
    pass


class LoginUser(LoginView):
    pass


def logout_user(request):
    logout(request)
    return redirect('login')

