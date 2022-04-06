from django.contrib import admin
from .models import TodoList, Todo

@admin.register(Todo)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('task', 'created', 'due_on', 'owner', 'mark','list_id')
    search_fields = ('task', 'mark','list_id')
    list_filter = ('task', 'created', 'due_on', 'owner', 'mark','list_id',)

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)