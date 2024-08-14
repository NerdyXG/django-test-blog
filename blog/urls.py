from django.urls import path
from .views import HomePageView, BlogDetailView, CreateNewBlogView, UpdateBlogView, DeleteBlogView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/new/', CreateNewBlogView.as_view(), name='new-blog'),
    path('blog/<int:pk>/edit/', UpdateBlogView.as_view(), name='edit-blog'),
    path('blog/<int:pk>/delete/', DeleteBlogView.as_view(), name='delete-blog'),
]
