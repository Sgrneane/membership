from django import forms
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class SignupForm(forms.ModelForm):         
            
    class Meta:
        model=CustomUser
        fields=['full_name','email','password']