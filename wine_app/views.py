from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator # Still useful for manual pagination if needed elsewhere
from django.db.models import Q
from django.views import generic # For class-based views like ListView
# No need to import User model directly if you're using request.user

from .models import WinePost, UserProfile
from .forms import WinePostForm, UserProfileForm # Ensure these forms are correctly defined

# --- Class-Based View for Home Page (Recommended) ---
class PostList(generic.ListView):
    """
    Displays a paginated list of published wine posts on the home page.
    """
    model = WinePost
    template_name = "wine_app/index.html" # Ensure this path is correct
    context_object_name = 'page_obj' # Name of the variable used in the template for the paginated posts
    paginate_by = 6

    def get_queryset(self):
        # Only show posts with status=1 (published) and order by creation date
        return WinePost.objects.filter(status=1).order_by('-created_on')

# --- Function-Based Views ---

def post_detail(request, slug):
    """
    Display an individual wine post.
    """
    # Using get_object_or_404 to retrieve the post, ensuring it's published (status=1)
    post = get_object_or_404(WinePost, slug=slug, status=1)

    return render(
        request,
        "wine_app/post_detail.html",
        {"post": post},
    )

@login_required
def create_post(request):
    """
    Allows a logged-in user to create a new wine post.
    """
    if request.method == "POST":
        form = WinePostForm(request.POST, request.FILES) # Add request.FILES if you handle images/files
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # Assign the current logged-in user as the author
            post.save()
            messages.success(request, "Post created successfully!")
            # Redirect to the detail page of the newly created post
            return redirect("wine_app:post_detail", slug=post.slug)
    else:
        form = WinePostForm()

    return render(
        request,
        "wine_app/create_post.html",
        {"form": form},
    )

@login_required
def update_post(request, slug):
    """
    Allows the author to update an existing wine post.
    """
    # Retrieve the post, ensuring the current user is the author
    post = get_object_or_404(WinePost, slug=slug, author=request.user)

    if request.method == "POST":
        form = WinePostForm(request.POST, request.FILES, instance=post) # Add request.FILES for updates
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            # Redirect to the updated post's detail page
            return redirect("wine_app:post_detail", slug=post.slug)
    else:
        form = WinePostForm(instance=post) # Populate form with existing post data

    return render(
        request,
        "wine_app/update_post.html",
        {"form": form, "post": post},
    )

@login_required
def delete_post(request, slug):
    """
    Allows the author to delete a wine post.
    """
    # Retrieve the post, ensuring the current user is the author
    post = get_object_or_404(WinePost, slug=slug, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully!")
        # Redirect to the home page after deletion
        return redirect("wine_app:home") # Ensure 'home' is the correct URL name for your home page

    return render(
        request,
        "wine_app/delete_post.html",
        {"post": post},
    )

# Placeholder views for other URLs you might have,
# if they are not handled by class-based views or specific functions.
# You'll need to implement the actual logic for these.

def blog(request):
    """
    Displays the main blog page. You might want to use a ListView here too,
    or simply redirect to the home page if it's the same content.
    """
    # Example: If blog page is just the home page, redirect
    return redirect('wine_app:home')
    # Or, if it's a different list of posts, define a new ListView or function
    # return render(request, 'wine_app/blog.html', {})

def login_view(request):
    """
    Handles user login. This typically uses Django's authentication views
    or a custom form.
    """
    # Example: You'll need actual login logic here
    return render(request, 'wine_app/login.html')

def register_view(request):
    """
    Handles user registration.
    """
    # Example: You'll need actual registration logic here
    return render(request, 'wine_app/register.html')

def profile(request):
    """
    Displays the user's profile.
    """
    # Example: You'll need to fetch user profile data
    return render(request, 'wine_app/profile.html', {})

def logout_view(request):
    """
    Handles user logout.
    """
    # Example: You'll need actual logout logic here
    # from django.contrib.auth import logout
    # logout(request)
    # messages.info(request, "You have been logged out.")
    # return redirect('wine_app:home')
    return render(request, 'wine_app/logout.html')