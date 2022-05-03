from articles.models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, generics, mixins, permissions


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    if request.method == 'POST': 
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, id):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT': 
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        article.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class ArticleMixinView(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      generics.GenericAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""class ArticleListAPIView(generics.ListAPIView):
       queryset = Article.objects.all()
       serializer_class = ArticleSerializer"""

class ArticleListCreateAPIView(generics.ListCreateAPIView): # can return list of article or create
       queryset = Article.objects.all()                        # new article depending on request method
       serializer_class = ArticleSerializer
       authentication_classes = [authentication.SessionAuthentication] # who is authenticated
       permission_classes = [permissions.IsAuthenticated] # who has permission to access this view

""" def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        body = serializer.validated_data.get('body') or None
        if body is None :
            body = title
        serializer.save(body=body)"""


class ArticleDetailAPIView(generics.RetrieveAPIView): # gets article details like function based view above also can
       queryset = Article.objects.all()
       serializer_class = ArticleSerializer
       lookup_field = 'pk'
    

class ArticleUpdateAPIView(generics.UpdateAPIView): # gets article details like function based view above also can
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()

class ArticleDeleteAPIView(generics.DestroyAPIView): # deletes article like function based view above also can
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
