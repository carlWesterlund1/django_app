from django.db import models
from django.contrib.auth.models import User

class Article (models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png", blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, null=True)
    #comment = models.ForeignKey(Article_comment, default=None, on_delete=models.SET_NULL, null=True)
    #   
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:20] + "..."

    def get_author(self):
        return self.author

class Article_comment (models.Model):
    title = models.CharField(max_length=100)
    #slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, default=None, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.body



