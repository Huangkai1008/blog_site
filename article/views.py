from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Article
from article.serializers import ArticleSerializer


# Create your views here.

class ArticleListView(APIView):
    """
    商品列表
    """
    def get(self, request):
        articles = Article.objects.all()
        article_serializer = ArticleSerializer(articles, many=True)
        return Response(article_serializer.data)
