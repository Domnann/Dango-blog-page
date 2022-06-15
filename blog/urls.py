from django.urls import path

from users.views import register
from .views import PostDetailView, PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name= 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name= 'post-detail'),
    path('about/', views.about, name='blog-about'),
    
]

