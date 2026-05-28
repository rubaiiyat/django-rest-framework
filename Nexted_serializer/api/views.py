from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics, mixins, status, viewsets

from employees.models import EmployeeModel
from api.serializer import EmployeeSerializer
from blogs.models import BlogsModel, CommentsModel
from blogs.serializer import BlogsSerializer, CommentsSerializer
# Create your views here.

class Employee(viewsets.ModelViewSet):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer


class Blogs(viewsets.ModelViewSet):
    queryset=BlogsModel.objects.all()
    serializer_class=BlogsSerializer

class Comments(viewsets.ModelViewSet):
    queryset=CommentsModel.objects.all()
    serializer_class=CommentsSerializer

   
    
    
""" class EmployeeDetail(viewsets.ModelViewSet):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer """
   

