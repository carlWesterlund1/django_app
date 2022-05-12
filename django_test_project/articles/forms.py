from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model=models.Article
        fields=['title', 'body', 'thumb']

class CreateComment(forms.ModelForm):
    class Meta:
        model=models.Article_comment
        fields=['title', 'body']

class SearchArticle(forms.ModelForm):
    class Meta:
        model=models.Article
        fields=['title']