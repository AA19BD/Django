import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Vacancy, Company
from api.serializers import CompanySerializer
# Create your views here.


@csrf_exempt
def list_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer=CompanySerializer(companies,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer=CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)


@csrf_exempt
def company_detail(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({"message": str(e)})
    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        try:
            company.name = data['name']
            company.description = data['description']
            company.city = data['city']
            company.address = data['address']
            company.save()  # updating new company item
        except Exception as e:
            return JsonResponse({"message": str(e)})
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({"message": "Item was deleted!"}, status=204)


def list_vacancies_by_company(request, pk):
    try:
        companies = Company.objects.get(id=pk)
        vac_by_companies = companies.vacancies.all()
        vac_by_companies_json = [i.to_json() for i in vac_by_companies]
    except Company.DoesNotExist as e:
        return JsonResponse({"message": str(e)})
    return JsonResponse(vac_by_companies_json, safe=False)


def list_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, pk):
    try:
        vacancy = Vacancy.objects.get(id=pk)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({"message": str(e)})
    return JsonResponse(vacancy.to_json())


def top_ten_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
