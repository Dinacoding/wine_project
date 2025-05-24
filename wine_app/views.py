from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    return HttpResponse("<h1>Welcome to the Wine App! This is the Home Page.</h1>")