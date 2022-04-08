import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from  products.models import Product
import sys
import os
sys.path.append(os.getcwd())
# Create your views here.

def api_home(request,*args,**kwargs):
    model_data=Product.objects.all().order_by('?').first()
    # data={}
    if model_data:
        data=model_to_dict(model_data,fields=['title','content','price'])
        # data['id']=model_data.id
        # data["title"]=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price
    return JsonResponse(data)

    # try:
    #     data=json.loads(request.body) #String of JSON data- >Python dict
    # except Exception as e:
    #     return JsonResponse({'message':str(e)})
    # data['params'] = dict(request.GET)#query param
    # data['headers'] = dict(request.headers)
    # # print(request.GET)#Url query param
    # return JsonResponse(data)