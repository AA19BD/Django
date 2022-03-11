from django.contrib import admin
from .models import TodoList, Todo

@admin.register(Todo)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('task', 'created', 'due_on', 'owner', 'mark',)
    search_fields = ('task', 'mark',)
    list_filter = ('task', 'created', 'due_on', 'owner', 'mark',)

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)