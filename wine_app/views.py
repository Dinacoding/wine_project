from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.views import generic # For potential future use of class-based views
from django.contrib.auth.models import User # Import User model for user_profile view

from .models import WinePost, UserProfile
from .forms import WinePostForm, UserProfileForm

# Create your views here.

def  home_page(request):
    """
    "Display the home page with a list of wine posts.

    """

    posts = WinePost.objects.filter(status=1).order_by('-created_on')
    
class PostList(generic.ListView):
    model = WinePost
    template_name = "wine_app/index.html"
    paginate_by = 6


def home_page(request):
    """
    Display the home page with a list of wine posts.
    """
    posts = WinePost.objects.filter(status=1).order_by('-created_on')
    
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "wine_app/index.html",
        {"page_obj": page_obj},
    )
def post_detail(request, slug):
    """
    Display an individual wine post.
    """
    post = get_object_or_404(WinePost, slug=slug, status=1)

    return render(
        request,
        "wine_app/post_detail.html",
        {"post": post},
    )
@login_required
def create_post(request):
    """
    Create a new wine post.
    """
    if request.method == "POST":
        form = WinePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect("wine_app:post_detail", slug=post.slug)
    else:
        form = WinePostForm()

    return render(
        request,
        "wine_app/create_post.html",
        {"form": form},
    )       