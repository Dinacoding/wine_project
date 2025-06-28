from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import WinePost
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect   
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages



class UserLoginView(LoginView):
    """
    View for user login
    """
    template_name = 'wine_app/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('blog')

class BlogListView(generic.ListView):
    """
    View for displaying list of wine posts in the blog
    """
    model = WinePost
    queryset = WinePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'wine_app/blog.html'
    context_object_name = 'wine_posts'
    paginate_by = 6

class UserLogoutView(LogoutView):
    """
    View for user logout
    """
    next_page = '/'
    http_method_names = ['get', 'post']# Redirect to home page after logout
    
class PostList(generic.ListView):
    """
    View for displaying list of wine posts
    """
    model = WinePost
    queryset = WinePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'wine_app/index.html'
    context_object_name = 'wine_posts'
    paginate_by = 6


def PostDetail(request, slug):
    """
    View for displaying a single wine post  
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
def delete_post(request, slug):
    post = get_object_or_404(WinePost, slug=slug)
    if request.user != post.author:
        messages.error(request, "You don't have permission to delete this post.")
        raise Http404("You don't have permission to delete this post")
    if request.method == 'POST':
        post_title = post.title
        post.delete()
        messages.success(request, f'Post "{post_title}" has been deleted successfully.')
        return redirect('blog')
    messages.warning(request, 'Invalid method for post deletion.')
    return redirect('post_detail', slug=slug)


    
class PostCreateView(generic.CreateView):
    """
    View for creating a new wine post
    """
    model = WinePost
    template_name = 'wine_app/post_detail.html'
    fields = ['title', 'wine_name', 'vintage_year', 'content', 'status']
    
    def form_valid(self, form):
        """
        If the form is valid, save the post and set the author to the current user
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

class UserRegisterView(generic.CreateView):
    """
    View for user registration
    """
    model = User  # Link to the Django User model
    template_name = 'wine_app/register.html'
    form_class = UserRegistrationForm  # <-- This line TELLS the CreateView to use YOUR form
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        """
        If the form is valid, save the user and redirect to the login page
        """
        user = form.save()
        return super().form_valid(form)
    
class HomeView(generic.TemplateView):
    """
    View for the home page
    """
    template_name = 'wine_app/index.html'



