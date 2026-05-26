from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    employee_id=models.CharField(max_length=10,unique=True)
    employee_name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    join_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.employee_name