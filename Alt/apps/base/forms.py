from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . import models
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ['username', 'surname', 'email', 'login', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'id': 'name', 'required': True, 'placeholder': 'Имя*'}),
            'surname': forms.TextInput(attrs={'id': 'surname', 'required': True, 'placeholder': 'Фамилия*'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'required': True, 'placeholder': 'Email*'}),
            'login': forms.TextInput(attrs={'id': 'login', 'required': True, 'placeholder': 'Логин*'}),
        }


class UserEditForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'surname', 'email', 'login', ]
        widgets = {
            'username': forms.TextInput(attrs={'id': 'platform_login', 'required': True, 'placeholder': 'Новое имя*'}),
            'surname': forms.TextInput(attrs={'id': 'platform_login', 'required': True, 'placeholder': 'Новая фамилия*'}),
            'email': forms.EmailInput(attrs={'id': 'platform_login', 'required': True, 'placeholder': 'Новый логин*'}),
            'login': forms.TextInput(attrs={'id': 'platform_login', 'required': True, 'placeholder': 'Новая почта*'}),
            'codeforces': forms.TextInput(attrs={'id': 'platform_login', 'required': True, 'placeholder': 'Новая почта*'}),
        }
