from django.shortcuts import render
from django.http import JsonResponse
from .models import Vacancy,Company
# Create your views here.

def list_companies(request):
    companies=Company.objects.all()
    companies_json=[company.to_json() for company in companies]
    return JsonResponse(companies_json,safe=False)

def company_detail(request,pk):
    try:
        company= Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({"message": str(e)})
    return JsonResponse(company.to_json())

def list_vacancies_by_company(request,pk):
    try:
        companies=Company.objects.get(id=pk)
        vac_by_companies=companies.vacancies.all()
        vac_by_companies_json=[i.to_json() for i in vac_by_companies]
    except Company.DoesNotExist as e:
        return JsonResponse({"message": str(e)})
    return JsonResponse(vac_by_companies_json,safe=False)
    
def list_vacancies(request):
    vacancies=Vacancy.objects.all()
    vacancies_json=[vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json,safe=False)

def vacancy_detail(request,pk):
    try:
        vacancy= Vacancy.objects.get(id=pk)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({"message": str(e)})
    return JsonResponse(vacancy.to_json())
    
def top_ten_vacancies(request):
    vacancies=Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json=[vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json,safe=False)
    