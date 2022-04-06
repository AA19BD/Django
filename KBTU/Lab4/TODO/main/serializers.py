from rest_framework import serializers
from .models import TodoList, Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','task','created','due_on','owner','mark','list_id')


class ListSerializer(serializers.ModelSerializer):
    # todos = TodoSerializer(read_only=True)
    class Meta:
        model = TodoList
        fields = '__all__'
