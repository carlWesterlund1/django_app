from django import forms
from . import models


class CreateUserProfile(forms.ModelForm):
    class Meta:
        model=models.UserProfile
        fields=['username', 'first_name', 'last_name']