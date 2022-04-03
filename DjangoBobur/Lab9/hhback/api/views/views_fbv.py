from django.http import JsonResponse
from ..models import Vacancy, Company
from ..serializers import CompanySerializer,CompanySerializer2
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET','POST'])
def list_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET','PUT','DELETE'])
def company_detail(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return Response({"message": str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer2(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer2(instance=company,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        company.delete()
        return Response({"message": "Item was deleted!"}, status=204)


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
