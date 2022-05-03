from django.urls import path
from .views import TodoListViewSet,TodoListViewSetById,ListViewSet,ListByIdViewSet,TodosByTodoList

urlpatterns = [
    path('todo_list/',TodoListViewSet.as_view({'get':'list','post':'create'})),
    path('todo_list/<int:pk>/',TodoListViewSetById.as_view({'get':'todo_list_by_id','put':'update'})),
    path('todos/', ListViewSet.as_view({'get': 'list','post': 'create'})),
    path('todos/<int:pk>/', ListByIdViewSet.as_view({'get': 'retrieve','put': 'update'})),
    path('todo_list/<int:pk>/todos/',TodosByTodoList.as_view({'get':'tasks_by_list'}))
]
