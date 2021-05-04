from django.shortcuts import render

# Create your views here.
def home_viewr(request):
    return render(request, 'testAppHtmls/home.html')

def movie_viewr(request):
    return render(request, 'testAppHtmls/movies.html')

def sports_viewr(request):
    return render(request, 'testAppHtmls/sports.html')

def politics_viewr(request):
    return render(request, 'testAppHtmls/politics.html')
