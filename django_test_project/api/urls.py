from django.urls import path, re_path
from . import views

app_name = 'api'
urlpatterns = [
    path(r'',views.article_list), 
    path('articles/<int:id>', views.article_detail)
    #re_path(r'(?P<slug>[\w-]+)', , name= ),
    
]