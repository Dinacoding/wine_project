# blog/views.py - CONSOLIDATED FROM YOUR VERSIONS (FIXED create_post)

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic # Removed 'View' as it's not strictly necessary if generic.View is not used directly
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages

# Import your forms (ensure WinePostForm is imported!)
from .forms import WinePostForm, UserRegistrationForm
from .models import WinePost  # Import the WinePost model


# --- Class-Based Views (from your provided code) ---

class UserLoginView(LoginView):
    """
    View for user login. Uses 'wine_app/login.html'.
    """
    template_name = 'wine_app/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('blog')

class BlogListView(generic.ListView):
    """
    View for displaying list of wine posts in the blog.
    Uses 'wine_app/blog.html'.
    """
    model = WinePost
    queryset = WinePost.objects.all().order_by('-updated_on')
    template_name = 'wine_app/blog.html'
    context_object_name = 'wine_posts'
    paginate_by = 6

class UserLogoutView(LogoutView):
    """
    View for user logout. Redirects to the blog page after logout.
    """
    next_page = '/'
    http_method_names = ['get', 'post']

class UserRegisterView(generic.CreateView):
    """
    View for user registration. Uses 'wine_app/register.html'.
    """
    model = User
    template_name = 'wine_app/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Account created successfully! Please log in.")
        return super().form_valid(form)

class HomeView(generic.TemplateView):
    """
    View for the home page. Uses 'wine_app/index.html'.
    """
    template_name = 'wine_app/index.html'


# --- Function-Based Views (from your provided code) ---

def PostDetail(request, slug): # Kept your original PostDetail function (capital P)
    """
    View for displaying a single wine post. Uses 'wine_app/post_detail.html'.
    Includes logic for incomplete fields as per your original snippet.
    """
    post = get_object_or_404(WinePost, slug=slug)
    incomplete_fields = []
    required_fields = {
        'title': post.title,
        'wine_name': post.wine_name,
        'vintage_year': post.vintage_year,
        'content': post.content,
        'status': post.status
    }
    for field_name, field_value in required_fields.items():
        if not field_value or (isinstance(field_value, str) and not field_value.strip()):
            incomplete_fields.append(field_name)

    context = {
        'post': post,
        'incomplete_fields': incomplete_fields,
    }
    return render(request, 'wine_app/post_detail.html', context)


@login_required
def create_post(request):
   
    if request.method == 'POST':
        form = WinePostForm(request.POST) # <--- CORRECTED THIS LINE
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = 1
            post.save()
            messages.success(request, f'Post "{post.title}" created successfully!')
            return redirect('post_detail', slug=post.slug) # Using 'post_detail' based on previous conversation
    else:
        form = WinePostForm()
    return render(request, 'wine_app/post_form.html', {'form': form})

@login_required
def delete_post(request, slug):
    """
    View for deleting a wine post. Only the post's author can delete it.
    """
    post = get_object_or_404(WinePost, slug=slug)

    if request.user != post.author:
        messages.error(request, "You don't have permission to delete this post.")
        raise Http404("You don't have permission to delete this post")

    if request.method == 'POST':
        post_title = post.title
        post.delete()
        messages.success(request, f'Post "{post_title}" has been deleted successfully.')
        return redirect('blog')

    messages.warning(request, 'Invalid method for post deletion. Please use the delete button.')
    return redirect('post_detail', slug=slug)

@login_required
def edit_post(request, slug):
    """
    View for editing a wine post. Only the post's author can edit it.
    """
    post = get_object_or_404(WinePost, slug=slug)

    if request.user != post.author:
        messages.error(request, "You don't have permission to edit this post.")
        raise Http404("You don't have permission to edit this post")

    if request.method == 'POST':
        form = WinePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'Post "{post.title}" updated successfully!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = WinePostForm(instance=post)

    return render(request, 'wine_app/post_form.html', {'form': form})