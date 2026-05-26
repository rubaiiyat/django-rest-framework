from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import mixins, status,generics

from employees.models import EmployeeModel
from api.serializer import EmployeeSerializer
# Create your views here.

class Employee(generics.ListCreateAPIView):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer

   
    
    
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer
   

