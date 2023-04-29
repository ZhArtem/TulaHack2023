from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'category', 'theme']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__input'}),
            'content': forms.Textarea(attrs={'cols': 40, 'rows': 20, 'class': 'form__input'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form__input'}),
            'category': forms.Select(attrs={'class': 'form__input'}),
            'theme': forms.Select(attrs={'class': 'form__input'}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form__input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form__input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form__input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form__input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__input'}))