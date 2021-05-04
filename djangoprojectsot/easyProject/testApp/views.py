from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.


'''def hello(request):
    s='<html><body><h1> Hello World of Django</h1></body></html>'
    return HttpResponse(s)'''

def hello(request):
    return render(request,'testAppHtmls/hello.html')
