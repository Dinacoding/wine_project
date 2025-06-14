from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import WinePost


class PostList(generic.ListView):
    """
    View for displaying list of wine posts
    """
    model = WinePost
    queryset = WinePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'wine_app/index.html'
    context_object_name = 'wine_posts'  # This will be available as 'wine_posts' in template
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
    model = WinePost  # This should be a User model, but using WinePost for example
    template_name = 'wine_app/register.html'
    form_class = None  # Replace with your User registration form
    success_url = '/'  # Redirect to home after successful registration

    def form_valid(self, form):
        # Handle user creation logic here
        return super().form_valid(form)
