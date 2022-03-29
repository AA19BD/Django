import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vacancy, Company
# Create your views here.


@csrf_exempt
def list_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.create(
                name=data['name'], description=data['description'], city=data['city'], address=data['address'])
        except Exception as e:
            return JsonResponse({"message": str(e)})
        return JsonResponse(company.to_json())


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
