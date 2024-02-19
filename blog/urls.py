from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('posts' ,views.getposts),
    path('post/create' ,views.createPost),
    path('post/like' ,  views.like_post),
    path('author/create' ,views.createAuthor),
    path('posts/singularpost/<int:id>/',views.extractpost),
    path('posts/singularpost/<int:id>/comments',views.getcomments),
    path('post/<int:id>/update', views.updatepost),
    path('post/delete-post/<int:pk>' , views.deletepost),
    path('post/status/<int:pk>' , views.change_status),
    path('posts/liked_posts',views.liked_posts)
]
