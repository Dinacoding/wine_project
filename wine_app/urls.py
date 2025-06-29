# wine_app/urls.py

from django.urls import path
from . import views


urlpatterns = [
    # General Pages / Auth (Class-Based Views)
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    # Post Management (Function-Based Views)
    path('post/create/', views.create_post, name='create_post'),
    path('post/<slug:slug>/', views.PostDetail, name='post_detail'), # Using PostDetail (capital P)
    path('post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
]