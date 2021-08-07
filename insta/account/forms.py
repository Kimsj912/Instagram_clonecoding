from django import forms
from .models import MyUser

class SignUpForm(forms.ModelForm):
    class Meta:
        model=MyUser
        fields =['email','name','username','password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder']=' 이메일을 입력하세요'
        self.fields['name'].widget.attrs['placeholder']=' 이름'
        self.fields['username'].widget.attrs['placeholder']=' 사용자 이름'
        self.fields['password'].widget.attrs['placeholder']=' 비밀번호'
        

class LoginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder']=' 이메일을 입력하세요'
        self.fields['password'].widget.attrs['placeholder']=' 비밀번호'
        