from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, PostModelForm, PostDeleteForm
from .models import Post, Comment, Tag, Author


def index(request):
    """Главная страница."""
    return render(request, template_name='blog_app/index.html')


def about(request):
    """Страница о нас."""
    return render(request, template_name='blog_app/about.html')


class PostBase:
    model = Post


class PostListView(PostBase, ListView):
    """Представление для отображения списка постов."""
    context_object_name = 'posts'
    extra_context = {'title': 'Список постов'}
    # model = Post
    # template_name = 'blog_app/post_list.html'

class PostDetailView(PostBase, DetailView):
    """Представление для отображения поста."""
    context_object_name = 'post'
    extra_context = {'title': 'Пост'}
    # model = Post
    # template_name = 'blog_app/post_detail.html'


class PostCreateView(PostBase, CreateView):
    """Представление для создания поста."""
    form_class = PostModelForm
    template_name = 'blog_app/post_add.html'
    success_url = reverse_lazy('post_list')
    # model = Post
    # template_name = 'blog_app/post_form.html'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Добавить пост'
    #     return context


class PostUpdateView(PostBase, UpdateView):
    """Представление для обновления поста."""
    form_class = PostModelForm
    template_name = 'blog_app/post_edit.html'
    success_url = reverse_lazy('post_list')
    # model = Post
    # template_name = 'blog_app/post_form.html'


class PostDeleteView(PostBase, DeleteView):
    """Представление для удаления поста."""
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')
    # model = Post

