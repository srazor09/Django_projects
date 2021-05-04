from django.shortcuts import render

# Create your views here.
def countview(request):
    count=int(request.COOKIES.get('count',0))
    newcount=count+1
    respone = render(request, 'testAppHtmls/count.html',{'count':newcount})
    respone.set_cookie('count',newcount,max_age=120)
    return respone
