from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg,Sum,Max,Min,Count
from testapp.models import Employee,ProxyEmployee,ProxyEmployee2
from django.db.models.functions import Lower


# Create your views here.
def display_view(request):
    # employees=Employee.objects.all()
    # employees=Employee.objects.all()
    employees=ProxyEmployee2.objects.all()
    #employees=Employee.objects.filter(ename__startswith='A')
    my_dict={'employees':employees}
    return render(request,'testapp/index.html',my_dict)
