
from django.core import paginator
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # For Pagination
from django.views.generic import ListView #For PostListView
from .forms import EmailPostForm # For Post Sharing
from .forms import CommentForm # For Comments   
# Create your views here.


def post_list(request):
    # Using our custom manager to get ONLY published posts
    posts = Post.published.all()
    pagn_obj = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = pagn_obj.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = pagn_obj.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = pagn_obj.page(pagn_obj.num_pages)
        
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request,year,month,day, post):
    # Try to find the post by ID, or return a 404 error
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             )

    # List of active comments for this post
    comments = post.comments.filter(active=True)
    
    # Form for users to comment
    form = CommentForm()

    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'form': form})
    

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False # <--- Track if email was sent
    
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            
            # ... send email 
            sent = True
            
    else:
        form = EmailPostForm()
        
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent
                                                    })

class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'