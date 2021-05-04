from django import forms

class nameForm(forms.Form):
    name=forms.CharField(max_length=30)

class ageForm(forms.Form):
    age=forms.IntegerField()

class GFForm(forms.Form):
    gf=forms.CharField(max_length=20)
