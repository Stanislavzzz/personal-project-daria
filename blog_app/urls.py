from django.urls import path
from .views import index, about, post_list, post_detail, post_add

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/add/', post_add, name='post_add'),
]
