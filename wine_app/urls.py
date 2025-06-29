from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('post/<slug:slug>/', views.PostDetail, name='post_detail'),
    path('post/create', views.PostCreateView.as_view(), name='create_post'),
    path('post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

]

