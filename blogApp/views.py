from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


# Create your views here.

def hello(request):
    return render(request, 'hello.html')


def home(request):
    return render(request, 'home.html')


def nothing(request):
    return HttpResponse("Nothing dey ")


def greet(request):
    posts = Post.objects.all()
    return render(request, 'hello.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


class post_list_view(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class post_detail_view(DetailView):
    model = Post
    template_name = 'post'


class post_create_view(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'author']
    success_url = reverse_lazy('hello2')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('hello2')


class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    context_object_name = 'post'
    fields = ['title', 'body']
    success_url = reverse_lazy('hello2')

