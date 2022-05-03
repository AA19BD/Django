from rest_framework import serializers
from .models import TodoList, Todo

class TodoSerializer(serializers.ModelSerializer):#va
    # todo_list=ListSerializer(read_only=True)
    class Meta:
        model = Todo
        fields = ('id','task','created','due_on','owner','mark','list_id','img','file')



class ListSerializer(serializers.ModelSerializer):#com
    todos = TodoSerializer(read_only=True)
    # todo = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = TodoList
        fields = ['title','todos']
