from django.shortcuts import render
import datetime

# Create your views here.
def tempView(request):
    date= datetime.datetime.now()
    MyDictionary={'date_msg' : date}
    return render(request, 'testApp/wish.html',context=MyDictionary)
