from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accountsapp.models import Customer


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]
class customeruserform(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'