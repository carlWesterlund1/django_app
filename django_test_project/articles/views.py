from django.shortcuts import render, redirect
from urllib3 import HTTPResponse
from .models import Article
from .models import Article_comment
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import get_user_model


def article_list(request):
    try:
        order = request.GET['sort_article']
    except:
        order = "date"
    if request.method == 'GET':
        articles = Article.objects.all().order_by(order)
    elif request.method == 'POST':
        articles = []
        form = forms.SearchArticle(request.POST) # Form for finding article matching user input
        if form.is_valid():
            instance = form.save(commit=False) # instance only for reference, doesn't save()
            for article in list(Article.objects.all()):
                if instance.title==article.title:
                    articles.append(article) # appending to list with matches
    
    search_form = forms.SearchArticle()
    return render(request, "articles/article_list.html", { 'articles': articles, 'search_form': search_form, 'order': order})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    author = article.get_author()
    try:
        comments = Article_comment.objects.filter(article=article) # Try to retrieve all comments already written
    except Article_comment.objects.all().DoesNotExist:
        comments = None    
    comment_form = forms.CreateComment()
    return render(request, 'articles/article_detail.html', {'article': article, "comments": comments, 'comment_form': comment_form, 'author': author})

def authors_articles(request): 
    articles = Article.objects.all() 
    authors = set()
    for article in articles:
        if article.author != None:
            authors.add(article.get_author()) # Adds the authors of articles to list article_authors. Articles can have same author so possible dublicates
    return render(request, 'articles/authors_articles.html', {'authors': authors, 'articles': articles}) # Renders as third parameter list of all the users who are authors and all articles


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user # The user who made article is made into author of article
            articles_titles = list(Article.objects.all().values_list('title', flat=True))
            if instance.title not in articles_titles: # to make sure no duplicate names or slugs
                instance.slug = instance.title
                instance.save() 
                return redirect('articles:list')
            else:
                nr = articles_titles.count(instance.title) # else block adds number to name/slug based on number of same-named articles
                instance.title = instance.title + "(" + str(nr) + ")"
                instance.slug = instance.title
                instance.save() 
                return redirect('articles:list')
    else: 
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})

@login_required(login_url="/accounts/login/")
def article_comment(request, slug):
    if request.method == 'POST':
        article = Article.objects.get(slug=slug) # Gets article user wants to comment
        comment = forms.CreateComment(request.POST, request.FILES)   
        if comment.is_valid():
            instance = comment.save(commit=False)
            instance.article = article
            instance.author = request.user # The user who made comment is made into author of comment
            instance.save() 
            return redirect('articles:detail', slug=slug)
        else:
            try:
                comments = Article_comment.objects.all() 
                pass
            except Article_comment.objects.all().DoesNotExist:
                comments = None
            return render(request, 'articles/article_detail.html', {'article': article, "comments": comments, 'comment': comment}) # returns error-messages for incorrectly filled form.
    else: 
        return redirect('articles:detail', slug=slug) # if user is redirected from loggin, correctly filled in form (any form) will render with error-messages. 
                                                      # Request.method=='POST' is then false.

@login_required(login_url="/accounts/login/") 
def article_modify(request, slug): 
    article = Article.objects.get(slug=slug) # Gets the article that should be modified 
    if request.method == 'POST':
        user = request.user 
        if user == article.get_author(): # Only user who is author of article can modify
            form = forms.CreateArticle(request.POST, instance=article) # Takes user input data and article that should be modified and 
            form.save() # updates article information
        else: HTTPResponse('cant update unless you are the author')
        return redirect('articles:detail', slug=slug)        
    else: # For GET requests. Takes existing Article and render an ArticleForm with prefilled fields that can be modified and send in POST request
        form = forms.CreateArticle(instance=article)
    return render(request, 'articles/article_modify.html', {'form': form, 'article':article})

    """From Stackoverflow: Every ModelForm also has a save() method. 
    This method creates and saves a database object from the data bound to the form. 
    A subclass of ModelForm can accept an existing model instance as the keyword argument instance; 
    if this is supplied, save() will update that instance. 
    If it’s not supplied, save() will create a new instance of the specified mode"""

