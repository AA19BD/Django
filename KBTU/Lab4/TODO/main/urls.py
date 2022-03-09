from django.contrib import admin
from django.urls import path
from .views import todo_list,todo_list_completed
urlpatterns = [
    path('todos/<int:id>/',todo_list,name="todos"),
    path('todos/<int:id>/completed/', todo_list_completed,name="completed"),
]
