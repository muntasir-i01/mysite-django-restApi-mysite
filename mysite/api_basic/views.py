from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# api_view decorator in function based api view 

@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many = True)
        return Response(serializer.data)

    
    elif request.method == 'POST':
        serializer = ArticleSerializers(data=request.data)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_CREATD)



@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == 'GET':
        serializer = ArticleSerializers(article)
        return JsonResponse(serializer.data)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializers(article, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)


    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
        

        
