from django import forms

class addItemForm(forms.Form):
    name=forms.CharField()
    quantity=forms.IntegerField()
    
