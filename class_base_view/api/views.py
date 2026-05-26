from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from employees.models import EmployeeModel
from api.serializer import EmployeeSerializer
# Create your views here.

class Employee(APIView):
    def get(self,request):
        employees=EmployeeModel.objects.all()
        serializer=EmployeeSerializer(employees, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    """ def get(self,request,id):
        employee=EmployeeModel.objects.get(pk=id)
        serializer=EmployeeSerializer(employee,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK) """
    
class EmployeeDetail(APIView):
    def get_object(self,pk):
        try:
            return EmployeeModel.objects.get(pk=pk)
        except EmployeeModel.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        employee=self.get_object(pk)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request,pk):
        employee=self.get_object(pk)
        serializer=EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        employee=self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

