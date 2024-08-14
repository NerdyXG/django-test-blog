from django.urls import path
from .views import HomePageView, BlogDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail')
]
