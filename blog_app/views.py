from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse

from .forms import PostForm, PostModelForm
from .models import Post, Comment, Tag, Author


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


# def post_add(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(
#                 title=form.cleaned_data['title'],
#                 content=form.cleaned_data['content'],
#                 rating=form.cleaned_data['rating'],
#                 author=Author.objects.first(),
#             )
#             return redirect('post_list')
#     else:
#         form = PostForm()
#
#     context = {
#         "title": "Добавить пост",
#         "form": form,
#     }
#     return render(request, template_name='blog_app/post_add.html', context=context)


def post_add(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm()

    context = {
        "title": "Добавить пост",
        "form": form,
    }
    return render(request, template_name='blog_app/post_add.html', context=context)



