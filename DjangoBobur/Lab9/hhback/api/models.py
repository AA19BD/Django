from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural='Companies'
        
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "city": self.city,
            "address": self.address
        }
        
class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    salary = models.FloatField(max_length=300)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,related_name="vacancies")
    
    
    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural='Vacancies'
    
    def to_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "salary": self.salary,
        }
    def __str__(self):
        return f'{self.id}-id|{self.name}| {self.description} |{self.salary}'
    
    