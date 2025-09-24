from django import forms
from django.contrib.auth.models import User
from TodoApp.models import Todo

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","email"]

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=["title","content","due_date"]