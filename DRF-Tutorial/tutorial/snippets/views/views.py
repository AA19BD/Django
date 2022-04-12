# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from ..models import Snippet
from ..serializers import SnippetSerializer

# @api_view(['GET','POST'])
class Snippetlist(APIView):
# def snippet_list(request,format=None):
    # if request.method == 'GET':
    def get(self,request,format=None):
        snippets=Snippet.objects.all()
        serializer=SnippetSerializer(snippets,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # elif request.method == 'POST':
    def post(self,request,format=None):
        # data=JSONParser.parse(request)
        serializer = SnippetSerializer(data=request.data)#can handle incoming json requests, but it can also handle other formats.
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

# @api_view(['GET','PUT','DELETE'])
class  SnippetDetail(APIView):
# def snippet_detail(request,pk,format=None):
    def get_object(self,pk):
        try:
           return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist as e:
            return Http404
            # return Response({'message':str(e)})

    def get(self,request,pk,format=None):
    # if request.method =='GET':
        snippet=self.get_object(pk)
        serializer=SnippetSerializer(snippet)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
    # elif request.method =='PUT':
        # data = JSONParser.parse(request)
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def delete(self,request,pk,format=None):
    # elif request.method == 'DELETE':
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








