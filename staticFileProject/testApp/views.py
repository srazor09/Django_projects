from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'testAppHtmls/home.html')

def profile(request):
    return render(request, 'testAppHtmls/profile.html')
