from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import WinePost
# Create your views here.

class PostList(generic.ListView):
    model = WinePost
    template_name = "wine_app/index.html"
    paginate_by = 6


def home_page(request):
    return HttpResponse("<h1>Welcome to the Wine App! This is the Home Page.</h1>")

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "wine_app/post_detail.html",
        {"post": post},
    )