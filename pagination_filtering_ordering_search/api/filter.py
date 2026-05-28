import django_filters
from employees.models import EmployeeModel

class EmployeeFilter(django_filters.FilterSet):
    position=django_filters.CharFilter(field_name='position',lookup_expr='iexact')
    emoloyee_id=django_filters.RangeFilter(field_name='employee_id',)

    class Meta:
        model=EmployeeModel
        fields=['position']