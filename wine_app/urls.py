from django.urls import path
from . import views
from django_summernote.admin import SummernoteModelAdmin
from django.views import generic
from .models import WinePost 


app_name = 'wine_app'

urlpatterns = [
    path('', views.home_page, name='home'),
]

class PostList(generic.ListView):
    queryset = WinePost.objects.filter(author=2)
    template_name = "post_list.html"