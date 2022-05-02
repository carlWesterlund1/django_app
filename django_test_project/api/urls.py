from django.urls import path, re_path
from . import views

app_name = 'api'
urlpatterns = [
    #path(r'',views.article_list), 
    #path(r'',views.ArticleListAPIView.as_view()),
    #path('articles/<int:id>', views.article_detail),
    path(r'articles/<int:pk>', views.ArticleDetailAPIView.as_view()),
    #re_path(r'(?P<slug>[\w-]+)', , name= ),
    path(r'',views.ArticleListCreateAPIView.as_view()),
    
]