from django.contrib.auth.models import User
from django import forms
from .models import People


class RegistForms1(forms.ModelForm):
    pw1=forms.CharField(widget=forms.PasswordInput,label='密码')
    pw2=forms.CharField(widget=forms.PasswordInput,label='重复密码')

    class Meta:
        model=User
        fields=['username']

    def clean_pw2(self):
        cd=self.cleaned_data
        if cd['pw1']!=cd['pw2']:
            raise forms.ValidationError('密码不匹配！')
        return cd['pw1']

class RegistForms2(forms.ModelForm):
    sex_choice=((0,'男'),(1,'女'))
    sex=forms.CharField(widget=forms.Select(choices=sex_choice),label='性别')



    class Meta:
        model=People
        fields=['name','age','sex','major','phone','prof']
