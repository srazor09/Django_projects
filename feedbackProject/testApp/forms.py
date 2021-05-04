from django import forms
from django.core import validators


#Validation to take only alpahabet not digit
"""def start_with_d(value):
    if value.isalpha() !=True:
        raise forms.ValidationError('Name should contain only aphabet')


#Email Validation to take gmail id only
def emai_vali(value):
    if value[len(value)-9:] !='gmail.com':
        raise forms.ValidationError("Must be gmail")"""

#using cleaned_data methodto validate email
"""def email_clean(self):
    inptemail=self.cleaned_data['email']
    print('Email Validation')
    return inptemail"""


""" Validation to take lower alphabet at start
 def start_with_d(value):
    if value[0].lower()!='d':
        raise forms.ValidationError('Name should start with d') """


"""class feedbackForm(forms.Form):
    name=forms.CharField(validators=[start_with_d])
    rollno=forms.IntegerField()
    email=forms.EmailField(validators=[emai_vali])
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])"""


#Validation all single form using clean method.
class feedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    #Total form validation
    def clean(self):
        print("Total form validation....")
        cleaned_data=super().clean()

        bot_handler_value=cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError("Thanks Bot..Please quit here now")

        inputpass = cleaned_data['password']
        inputrpass = cleaned_data['rpassword']
        if inputpass != inputrpass:
            raise forms.ValidationError('Passwords not matched')

        inputname=cleaned_data['name']
        if len(inputname) < 10:
            raise forms.ValidationError('Name should compulsory conatains minimum 10 characters')

        inputrollno=cleaned_data['rollno']
        if len(str(inputrollno)) !=3:
            raise forms.ValidationError(('Roll no should contain exactly 3 digits'))





#Explicit Validations are below

"""    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError('Length should be greater than 4 for name ')
        return inputname

    def clean_rollno(self):
        inprollno=self.cleaned_data['rollno']
        print('validating rollno')
        return inprollno

    def clean_email(self):
        inpemail=self.cleaned_data['email']
        print('validating email')
        return inpemail

    def clean_feedback(self):
        inpfeedback=self.cleaned_data['feedback']
        print('validating feedback')
        return inpfeedback
"""
