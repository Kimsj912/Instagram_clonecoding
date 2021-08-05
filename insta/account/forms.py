from django import forms
from .models import userInfo

class UserForm(forms.ModelForm):
    class Meta:
        model=userInfo
        fields =['username','email','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = userInfo
        fields = ['username', 'password']