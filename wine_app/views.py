from django.shortcuts import render
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