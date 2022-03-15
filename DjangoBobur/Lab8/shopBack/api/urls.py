from django.contrib import admin
from django.urls import path
from .views import products_list,product_detail

urlpatterns = [
    path("products",products_list,name="products_list"),
    path("products/<int:pk>",product_detail,name="product_detail")
]
