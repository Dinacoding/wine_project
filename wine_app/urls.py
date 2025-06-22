from django.urls import path
from . import views

class HomeView(views.generic.TemplateView):
    template_name = 'wine_app/home.html'
    
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]

