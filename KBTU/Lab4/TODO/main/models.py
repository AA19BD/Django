from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    title = models.CharField(max_length=100)


class Todo(models.Model):
    task = models.CharField(max_length=100)
    created = models.DateTimeField(default=None, null=True, blank=True)
    due_on = models.DateTimeField(default=None, null=True, blank=True)
    owner = models.CharField(max_length=100)
    mark = models.BooleanField(default=True)
    list_id = models.ForeignKey(TodoList, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ('task',)