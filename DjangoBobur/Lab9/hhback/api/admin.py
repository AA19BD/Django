from django.contrib import admin
from .models import Vacancy,Company
# Register your models here.




@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display= ('name','description','salary','company')
    list_filter=('name','description','salary','company')
    search_fields=('name','description','salary','company')
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display= ('name','description',"city","address")
    list_filter=('name','description',"city","address")
    search_fields=('name','description',"city","address")