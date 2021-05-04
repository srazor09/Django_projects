from django.shortcuts import render
from testApp.forms import addItemForm

# Create your views here.
def add_item_view(request):
    form=addItemForm()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
        #request.session.set_expiry(60) #Expire session in seconds
        #request.session.set_expiry(0) #Expire session when browser closed
    return render(request, 'testAppHtmls/additem.html', {'form':form})

def disp_item_view(request):
    return render(request, 'testAppHtmls/displayitem.html')

def session_info_view(request):
    session=request.session
    age=session.get_expiry_age()
    date=session.get_expiry_date()
    print('Age',age)
    print('Expiry Date : ',date)
    return render(request, 'testAppHtmls/additem.html')
