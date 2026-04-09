from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post_list(request):
    # Using our custom manager to get ONLY published posts
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})