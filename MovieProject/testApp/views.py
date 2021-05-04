from django.shortcuts import render
from testApp import forms
from testApp.models import Movie

# Create your views here.

def indexasView(request):
    return render(request, 'testAppHtmls/index.html')

def addMovieView(request):
    form=forms.MovieForm()
    if request.method=='POST':
        form=forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return indexasView(request)
    return render(request, 'testAppHtmls/addmovies.html',{'form':form})

def listMovieView(request):
    movies_list=Movie.objects.all()
    return render(request, 'testAppHtmls/listmovies.html',{'movies_list':movies_list})
