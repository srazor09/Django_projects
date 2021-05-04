from django.shortcuts import render
from testApp.models import filterModel

# Create your views here.

def upper_view(request):
    data_list=filterModel.objects.all()
    return render(request, 'testAppHtmls/upper.html',{'data_list': data_list})


def lower_view(request):
    data_list=filterModel.objects.all()
    return render(request, 'testAppHtmls/lower.html',{'data_list': data_list})

def truncate_view(request):
    data_list=filterModel.objects.all()
    return render(request, 'testAppHtmls/truncate.html',{'data_list': data_list})
