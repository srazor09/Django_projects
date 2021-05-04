from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg,Sum,Max,Min,Count
from testapp.models import Employee,ProxyEmployee,ProxyEmployee2
from django.db.models.functions import Lower


# Create your views here.
def display_view(request):
    #employees=Employee.objects.all()
    #employees=Employee.objects.filter(ename__istartswith='A')
    #employees=Employee.objects.exclude(~Q(ename__startswith='J'))
    """qs1=Employee.objects.filter(esal__lt=18000)
    qs2=Employee.objects.filter(ename__endswith='N')
    employees=qs1.union(qs2)
    print(qs1.count())
    print(qs2.count())
    print(employees.count())
    print(employees.query)"""
    """avg=Employee.objects.all().aggregate(Avg('esal'))
    max=Employee.objects.all().aggregate(Max('esal'))
    min=Employee.objects.all().aggregate(Min('esal'))
    sum=Employee.objects.all().aggregate(Sum('esal'))
    count=Employee.objects.all().aggregate(Count('esal'))"""
    #my_dict={'avg':avg,'max':max,'min':min,'sum':sum,'count':count}
    #employees=Employee.objects.filter(esal__lt=18000)
    employees=Employee.objects.all()
    #employees=Employee.objects.all().order_by('eno')  #Ascending order
    #employees=Employee.objects.all().order_by('-esal')[:5] #Descending order
    #employees=Employee.objects.all().order_by(Lower('ename'))
    print(employees.count())
    #qs=Employee.objects.filter(esal__gt=15000)
    #qs.delete
    #employees=Employee.objects.all().values('eno','esal')
    #employees=Employee.objects.all().only('eno','esal')
    # employees=Employee.objects.all()
    #employees=ProxyEmployee2.objects.all()
    #employees=Employee.objects.filter(ename__startswith='A')
    my_dict={'employees':employees}
    return render(request,'testapp/index.html',my_dict)
    #return render(request,'testapp/aggregate.html',my_dict)
