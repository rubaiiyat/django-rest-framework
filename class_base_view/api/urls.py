from django.urls import path
from api.views import Employee, EmployeeDetail


urlpatterns = [
    path('employees/',Employee.as_view()),
    path('employee/<int:pk>',EmployeeDetail.as_view()),
]


