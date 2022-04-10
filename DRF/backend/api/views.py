import json
import sys
import os
sys.path.append(os.getcwd())
from django.forms.models import model_to_dict
# from django.http import JsonResponse
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from  products.models import Product
from  products.serializers import ProductSerializer

@api_view(["GET","POST"])
def api_home(request,*args,**kwargs):
    instance=Product.objects.all().order_by('?').first()
    # data={}
    if instance:
        # data=model_to_dict(model_data,fields=['title','content','price','sale_price'])
        data=ProductSerializer(instance).data
        # data['id']=model_data.id
        # data["title"]=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price
    return Response(data)

    # try:
    #     data=json.loads(request.body) #String of JSON data- >Python dict
    # except Exception as e:
    #     return JsonResponse({'message':str(e)})
    # data['params'] = dict(request.GET)#query param
    # data['headers'] = dict(request.headers)
    # # print(request.GET)#Url query param
    # return JsonResponse(data)