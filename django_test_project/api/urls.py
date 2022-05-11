from django.urls import path, re_path
from . import views

app_name = 'api'
urlpatterns = [
    #path(r'',views.article_list), 
    #path(r'',views.ArticleListAPIView.as_view()),
    #path('articles/<int:id>', views.article_detail),
    path(r'details/<int:pk>', views.ArticleDetailAPIView.as_view()),
    path(r'',views.ArticleListCreateAPIView.as_view()), # article list if get, create new article if post
    path(r'update/<int:pk>', views.ArticleUpdateAPIView.as_view()),
    path(r'delete/<int:pk>', views.ArticleDeleteAPIView.as_view()),    
]