from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testApp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request, 'testAppHtmls/home.html')

@login_required
def javaexams_view(request):
    return render(request, 'testAppHtmls/javaexams.html')

@login_required
def pyexams_view(request):
    return render(request, 'testAppHtmls/pythonexams.html')

@login_required
def aptexams_view(request):
    return render(request, 'testAppHtmls/aptiexams.html')

def logout_view(request):
    return render(request, 'registration/logout.html')

def sign_up_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        """if form.is_valid():  #Method -1 You can also use this to store password in encrypted form
            form.save() """
        #form.save() - Dont use this as this will not store password in encrypted form.
        user=form.save()
        user.set_password(user.password) #Method -2 this will take care of hashing
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'registration/signup.html',{'form':form})
