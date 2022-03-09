from django.shortcuts import render
from .models import Todo, TodoList
from django.views.generic import DeleteView

def todo_list(request, id):
    tasks = Todo.objects.filter(list_id=id)
    list = TodoList.objects.get(id=id)
    context = {
        'tasks': tasks,
        'list': list
    }
    return render(request, 'main/todo_list.html', context=context)

def todo_list_completed(request, id):
    tasks = Todo.objects.filter(list_id=id, mark=True)
    list = TodoList.objects.get(id=id)
    context = {
        'tasks': tasks,
        'list': list
    }
    return render(request, 'main/completed_todo_list.html', context=context)

