from .models import Todo, TodoList
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ListSerializer,TodoSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list' or  self.action=="create":
            return ListSerializer
        return TodoSerializer

class TasksByListViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    @action(methods=['GET'], detail=False, permission_classes=(IsAuthenticated,))
    def tasks_by_list(self, request, pk):
        queryset = Todo.objects.filter(list_id=pk)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)


class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    @action(methods=['GET'], detail=False, permission_classes=(IsAuthenticated,))
    def completed_tasks(self, request, pk):
        queryset = Todo.objects.filter(list_id=pk).filter(mark=True)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

