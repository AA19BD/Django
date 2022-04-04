from unicodedata import name
from django.contrib import admin
from django.urls import path
#from .views import list_companies,company_detail,list_vacancies,vacancy_detail,list_vacancies_by_company,top_ten_vacancies
from .views import CompaniesListAPIView,CompanyDetailAPIView,VacancyListAPIView,VacancyDetailAPIView

urlpatterns = [
    path('companies/',CompaniesListAPIView.as_view(),name='list_companies'),
    path('companies/<int:pk>',CompanyDetailAPIView.as_view(),name='company_detail'),
    # path('companies/<int:pk>/vacancies',list_vacancies_by_company,name='list_vacancies_by_company'),
    path('vacancies/',VacancyListAPIView.as_view(),name='list_vacancies'),
    path('vacancies/<int:pk>',VacancyDetailAPIView.as_view(),name='vacancy_detail')
    # path('vacancies/top_ten',top_ten_vacancies,name='top_ten_vacancies')
]
