from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Company
from ..serializers import CompanySerializer2
from rest_framework import status

class CompaniesListAPIView(APIView):

    def get(self,request):
        companies = Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailAPIView(APIView):

    def get_object(self,pk):
        try:
            return Company.objects.get(id=pk)
        except Company.DoesNotExist as e:
            return Http404

    def get(self,request,pk=None):
        companies=self.get_object(pk)
        serializer = CompanySerializer2(companies)
        return Response(serializer.data)

    def put(self,request,pk=None):
        company=self.get_object(pk)
        serializer = CompanySerializer2(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk=None):
        company=self.get_object(pk)
        company.delete()
        return Response({"message": "Item was deleted!"}, status=204)


