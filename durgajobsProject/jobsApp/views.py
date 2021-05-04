from django.shortcuts import render
from jobsApp.models import *
#from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'testAppHtmls/index.html')

def hydjobsinfo(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list': jobs_list}
    return render(request, 'testAppHtmls/hydjobs.html', context=my_dict)

def punejobsinfo(request):
    s='<h1>Pune Jobs Information</h1>'
    return HttpResponse(s)

def bangljobsinfo(request):
    s='<h1>Banglore Jobs Information</h1>'
    return HttpResponse(s)

def chennaijobsinfo(request):
    s='<h1>Chennai Jobs Information</h1>'
    return HttpResponse(s)
