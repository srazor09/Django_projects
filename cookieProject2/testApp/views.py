from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request, 'testAppHtmls/name.html')

def age1_view(request):
    name=request.GET['name']  #reading data from name.html
    response = render(request, 'testAppHtmls/age.html')
    response.set_cookie('name',name)
    return response

def gf_view(request):
    age=request.GET['age']
    response = render(request, 'testAppHtmls/girlfriend.html')
    response.set_cookie('age',age)
    return response

def resultss_view(request):
    gfname=request.GET['gf']
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    #gfname=request.POST.get('gfname',False)
    response=render(request, 'testAppHtmls/results.html', {'name':name,'age':age,'gfname':gfname})
    return response
