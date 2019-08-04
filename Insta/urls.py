#manage app's urls

from django.contrib import admin
from django.urls import include, path

from Insta.views import HelloWorld, PostDetailView, PostsView

urlpatterns = [
    path('', HelloWorld.as_view(), name='helloworld'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
