from django.urls import path
from . import views

app_name = 'wine_app'

urlpatterns = [ # <--- THIS MUST BE A LIST!
    # Add your URL patterns here. At least one is usually needed.
    path('', views.home_page, name='home'), # Example path
    # path('wines/', views.wine_list, name='wine_list'), # Another example
    # path('wines/<slug:wine_slug>/', views.wine_detail, name='wine_detail'),
]
