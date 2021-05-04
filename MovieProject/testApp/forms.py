from django import forms
from testApp.models import Movie

class MovieForm(forms.ModelForm):
    #Field codes will be here.
    class Meta:
        model=Movie
        fields='__all__'
