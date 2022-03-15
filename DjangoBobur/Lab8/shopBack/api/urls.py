from django.contrib import admin
from django.urls import path
from .views import products_list,product_detail,categories_list,category_detail

urlpatterns = [
    path("products",products_list,name="products_list"),
    path("products/<int:pk>",product_detail,name="product_detail"),
    path('categories/',categories_list,name="categories_list"),
    path('categories/<int:pk>',category_detail, name="categories_list"),

]
