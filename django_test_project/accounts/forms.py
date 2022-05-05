from xml.etree.ElementInclude import include
from . import models
from django.contrib.auth.forms import UserCreationForm  
from django import forms


class CreateUserProfile(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        include = ['description', 'profile_pic']
