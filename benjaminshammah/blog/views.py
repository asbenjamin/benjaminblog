from django.shortcuts import render
from .models import Post

# Create your views here.

class PostListView():
    model = Post

class PostCreateView():
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")

class PostDetailView():
    model = Post

class PostUpdateView():
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")

class PostDeleteView():
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")
