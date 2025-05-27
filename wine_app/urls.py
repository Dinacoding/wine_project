from django.urls import path
from . import views

app_name = 'wine_app'

urlpatterns = [
    path('', views.home_page, name='home'),
]
