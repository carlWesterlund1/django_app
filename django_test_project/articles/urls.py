"""django_test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views

app_name = 'articles'
urlpatterns = [
    path(r'', views.article_list, name='list'), 
    path(r'create', views.article_create, name='create'),
    path(r'authors_articles', views.authors_articles, name='authors_articles'),
    re_path(r'comment/(?P<slug>[\w-]+)', views.article_comment, name='comment'),
    re_path(r'modify/(?P<slug>[\w-]+)', views.article_modify, name='modify'),
    re_path(r'(?P<slug>[\w-]+)', views.article_detail, name="detail" ),
    
]
