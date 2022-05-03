import logging
from django.shortcuts import get_object_or_404
from .models import Todo, TodoList
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ListSerializer,TodoSerializer
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

logger = logging.getLogger(__name__)

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list' or  self.action=="create":
            logger.info("List has been used/created!")
            return ListSerializer
        return TodoSerializer

class TodoListViewSetById(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer

    @action(methods=['GET','POST'], detail=False, permission_classes=(IsAuthenticated,))
    def todo_list_by_id(self, request, pk=None):
        queryset = TodoList.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ListSerializer(user)
        logger.info('TodoList was received/created by id!')
        return Response(serializer.data)

class ListViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser, JSONParser,)

class ListByIdViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

class TodosByTodoList(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], detail=False, permission_classes=(IsAuthenticated,))
    def tasks_by_list(self, request, pk):
        queryset = Todo.objects.filter(list_id=pk)
        serializer = TodoSerializer(queryset, many=True)
        logger.info("TodosByTodoList was used!")
        return Response(serializer.data)



