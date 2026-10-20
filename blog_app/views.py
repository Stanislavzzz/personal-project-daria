from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Post, Comment, Tag


def index(request):
    """Главная страница."""
    return render(request, template_name='blog_app/index.html')


def about(request):
    """Страница о нас."""
    return render(request, template_name='blog_app/about.html')


def post_list(request):
    """Страница со списком постов."""
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Список постов'
    }
    return render(request, template_name='blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    """Страница с постом."""
    post = get_object_or_404(Post, pk=post_id)
    # post = Post.objects.get(pk=post_id)
    comments = post.comments.all()
    tags = post.tags.all()
    context = {
        'post': post,
        'title': post.title,
        'comments': comments,
        'tags': tags,
    }
    return render(request, template_name='blog_app/post_detail.html', context=context)