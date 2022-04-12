from ..models import Snippet
from ..serializers import SnippetSerializer
from rest_framework import mixins,generics

class Snippetlist(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

