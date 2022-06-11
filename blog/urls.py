from django.urls import path

from users.views import register
from . import views

urlpatterns = [
    path('', views.home, name= 'blog-home'),
    path('about/', views.about, name='blog-about'),
    
]

