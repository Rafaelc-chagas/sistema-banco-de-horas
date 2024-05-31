from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import EmployeeUser


class EmployeeUserCreationForm(UserCreationForm):
    class Meta:
        model = EmployeeUser
        fields = ('cpf', 'email', 'full_name')


class EmployeeUserChangeForm(UserChangeForm):
    class Meta:
        model = EmployeeUser
        fields = ('cpf', 'email', 'full_name', 'is_active', 'is_staff')


class CPFLoginForm(AuthenticationForm):
    username = forms.CharField(label='CPF', max_length=11)
