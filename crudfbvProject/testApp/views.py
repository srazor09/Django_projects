from django.shortcuts import render
from testApp.models import Employee
from testApp.forms import EmployeeForm
from django.http import HttpResponseRedirect


# Create your views here.

#Select or only list out the data from database
def retrieve_view(request):
    employees=Employee.objects.all()
    return render(request, 'testAppHtmls/index.html',{'employees':employees})

#Create Records and display
def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/$')
    return render(request, 'testAppHtmls/create.html',{'form':form})

#Delete records and display
def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect('/$')

#Update your records and display
def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=Employee(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/$')
    return render(request, 'testAppHtmls/update.html',{'employee':employee})
