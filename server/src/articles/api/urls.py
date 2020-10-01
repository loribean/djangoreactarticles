from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path("art", ArticleListView.as_view()),
    path("<pk>", ArticleDetailView.as_view()),

    
]