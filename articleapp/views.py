from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import *
from .serializers import *

@csrf_exempt
@api_view(['GET', 'POST','PATCH'])
def article_api(request):
	"""
	List all code snippets, or create a new snippet.
	"""
	if request.method == 'GET':
		articles = Article.objects.all().order_by('-vote')
		serializer = ArticleSerializer(articles, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'PATCH':
		id = request.data['id']
		article = Article.objects.get(id=id)
		serializer = ArticleSerializer(article,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)