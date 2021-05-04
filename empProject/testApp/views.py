from django.shortcuts import render
from testApp.models import Employee
#from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'testAppHtmls/index.html')

def empview(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list' : emp_list}
    return render(request, 'testAppHtmls/emp.html', context=my_dict)
