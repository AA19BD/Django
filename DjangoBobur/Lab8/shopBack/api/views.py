from django.http import JsonResponse
from django.shortcuts import render
from .models import Product


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

