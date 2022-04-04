from rest_framework import serializers
from .models import Company,Vacancy

# class CompanySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=300)
#     description = serializers.CharField(max_length=300)
#     city = serializers.CharField(max_length=100)
#     address = serializers.CharField(max_length=100)
#
#     def create(self,validated_data):
#         company=Company.objects.create(**validated_data)
#         return company
#
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name')
#         instance.description=validated_data.get('description')
#         instance.city=validated_data.get('city')
#         instance.address=validated_data.get('address')
#         instance.save()#saving to database
#         return instance

class CompanySerializer2(serializers.ModelSerializer):#BaseSerializer

    # vacancies=serializers.PrimaryKeyRelatedField(many=True, read_only=True)#Company.vacancies.all()
    vacancies = serializers.StringRelatedField(many=True, read_only=True)#Company.vacancies.all()
    class Meta:
        model=Company
        fields=('id','name','description','city','address','vacancies')

class VacancySerializer(serializers.ModelSerializer):
    company=CompanySerializer2(read_only=True)#Inheritance from BaseSerializer->(Nested objects)
    # company_id=serializers.IntegerField(read_only=True)
    class Meta:
        model=Vacancy
        fields=('id','name','description','salary','company')