from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    snippet = serializers. SerializerMethodField(read_only=True)
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 
                 'body', 'date', 'thumb', 
                 'author', 'snippet']
    
    def get_snippet(self, obj):
        return obj.snippet()
  