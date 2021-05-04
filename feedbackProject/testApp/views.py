from django.shortcuts import render
from . import forms

# Create your views here.

def feedback_view(request):
    form=forms.feedbackForm()
    if request.method=='POST':
        form=forms.feedbackForm(request.POST)
        if form.is_valid():
            print('Form validation success and printing feedback information')
            print('Student Name :',form.cleaned_data['name'])
            print('Student RollNo :',form.cleaned_data['rollno'])
            print('Student Email_id :',form.cleaned_data['email'])
            print('Student Feedback :',form.cleaned_data['feedback'])
            return render(request, 'testAppHtmls/thankyou.html',{'name':form.cleaned_data['name']})


    return render(request, 'testAppHtmls/feedback.html', {'form': form})
