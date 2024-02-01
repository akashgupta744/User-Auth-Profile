from django import forms
from .models import *
from django.forms.widgets import FileInput
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets={'password1':forms.PasswordInput}
        help_texts = {'username':''}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'profile_img' : FileInput(),
            'phone_no': forms.TextInput(attrs = {'placeholder':'xxxxx-xxxxx'})
        }