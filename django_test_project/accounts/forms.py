from xml.etree.ElementInclude import include
from . import models
from django.contrib.auth.forms import UserCreationForm  
from django import forms


class CreateUserProfile(forms.ModelForm):
    
    class Meta():
        model=models.Profile
        fields=['name', 'profile_pic', 'description'] 
        
    
    
