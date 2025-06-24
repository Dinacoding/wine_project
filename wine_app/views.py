from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import WinePost
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect



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
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return redirect('home')
    
class PostList(generic.ListView):
    """
    View for displaying list of wine posts
    """
    model = WinePost
    queryset = WinePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'wine_app/index.html'
    context_object_name = 'wine_posts'
    paginate_by = 6

class PostDetail(generic.DetailView):
    """
    View for displaying individual wine post
    """
    model = WinePost
    template_name = 'wine_app/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return WinePost.objects.filter(status=1)

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