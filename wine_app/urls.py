from django.urls import path
from . import views
from django_summernote.admin import SummernoteModelAdmin
from django.views import generic
from .models import WinePost 


app_name = 'wine_app'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog/', views.blog, name='blog'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),  
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/list/', views.PostList.as_view(), name='post_list'),
]


class PostList(generic.ListView):
    queryset = WinePost.objects.filter(author=2)
    template_name = "post_list.html"