from django.http import JsonResponse
from django.shortcuts import render
from .models import Product,Category


# Create your views here.
def products_list(request):
    products = Product.objects.all()#Select * from api.product
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json,safe=False)#safe=false since we have multiple items


def product_detail(request,pk):
    try:
        product = Product.objects.get(id=pk)#Select * from api.product where id =pk
    except Product.DoesNotExist as e:
        return JsonResponse({"message": str(e)})
    return JsonResponse(product.to_json())

def categories_list(rrequest):
    categories = Category.objects.all()#Select * from api.category
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json,safe=False)#safe=false since we have multiple items

def category_detail(request,pk):
    try:
        category = Category.objects.get(id=pk)#Select * from api.category where id =pk
    except Category.DoesNotExist as e:
        return JsonResponse({"message": str(e)})
    return JsonResponse(category.to_json())