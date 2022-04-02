from rest_framework import serializers
from api.models import Company

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length=300)
    city = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)

    def create(self,validated_data):
        company=Company.objects.create(**validated_data)
        return company
# company = Company.objects.create(#**data-kwargs
 #  name=data['name'], description=data['description'], city=data['city'], address=data['address'])