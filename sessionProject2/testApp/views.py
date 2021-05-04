from django.shortcuts import render

from testApp.forms import nameForm,ageForm,GFForm

# Create your views here.

def name_view(request):
    form=nameForm()
    return render(request, 'testAppHtmls/name.html',{'form':form})

def age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=ageForm()
    return render(request, 'testAppHtmls/age.html',{'form':form})

def gf_view(request):
    age=request.GET['age']
    request.session['age']=age
    form=GFForm()
    return render(request, 'testAppHtmls/gf.html',{'form':form})

def resul_view(request):
    gf=request.GET['gf']
    request.session['gf']=gf
    #form=ageForm()
    return render(request, 'testAppHtmls/results.html')
