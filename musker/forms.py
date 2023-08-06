from django import forms 
from .models import Meep 

class MeepForm(forms.ModelForm):
    body=forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder":"Enter your musker meep!", 
                "class":"form-controll",
            }
        ),  
        label="", 
    ) 

    class Meta:
        model=Meep 
        exclude=("user",) 