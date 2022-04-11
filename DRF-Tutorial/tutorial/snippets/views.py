# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer

@api_view(['GET','POST'])
def snippet_list(request,format=None):
    if request.method == 'GET':
        snippets=Snippet.objects.all()
        serializer=SnippetSerializer(snippets,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # data=JSONParser.parse(request)
        serializer = SnippetSerializer(data=request.data)#can handle incoming json requests, but it can also handle other formats.
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk,format=None):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist as e:
        return Response({'message':str(e)})

    if request.method =='GET':
        serializer=SnippetSerializer(snippet)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method =='PUT':
        # data = JSONParser.parse(request)
        serializer = SnippetSerializer(snippet,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








