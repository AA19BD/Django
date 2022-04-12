from django.urls import path
# from .views import snippet_detail,snippet_list
from .views import Snippetlist,SnippetDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns=[
    path('snippets',Snippetlist.as_view()),
    path('snippets/<int:pk>/',SnippetDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)