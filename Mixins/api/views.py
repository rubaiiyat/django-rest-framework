from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import mixins, status,generics

from employees.models import EmployeeModel
from api.serializer import EmployeeSerializer
# Create your views here.

class Employee(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    
class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(pk)
   

