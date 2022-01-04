from django.urls import path
from . import views



urlpatterns = [
    path('',views.news_home,name='news_home'),#method
    path('create', views.create, name='create'),#method
    path('<int:pk>',views.NewsDetailView.as_view(),name="news-detail"),#pk->Primary key->class
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name="news-update"),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name="news-delete")

]
