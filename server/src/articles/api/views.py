from rest_framework.generics import ListAPIView, RetrieveAPIView
from articles.models import Article
from .serializers import ArticleSerializer
from django.http import HttpResponseRedirect
from rest_framework import generics, status
from rest_framework.response import Response

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def post(self,request,format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect('/')



class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
