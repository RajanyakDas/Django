from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post_list(request):
    # Using our custom manager to get ONLY published posts
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, id):
    # Try to find the post by ID, or return a 404 error
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})