from django.urls import path
from .views import ListViewSet,TasksByListViewSet,CompletedTaskViewSet


urlpatterns = [
    path('todos/', ListViewSet.as_view({'get': 'list','post': 'create'})),
    path('todos/<int:pk>/', TasksByListViewSet.as_view({'get': 'tasks_by_list',
                                                        'post': 'create',
                                                        'put': 'update',
                                                        'delete': 'destroy'})),
    path('todos/<int:pk>/completed/', CompletedTaskViewSet.as_view({'get': 'completed_tasks'}))
]