from django.shortcuts import render
from testApp import forms
# Create your views here.
def studentview(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Form submitted successfully')
    return render(request, 'testAppHtmls/register.html', {'form':form})
