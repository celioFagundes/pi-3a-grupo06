# app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email'})
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'})
    )

    password2 = forms.CharField(
        label='Confirme a Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'})
    )

    class Meta:
        model = CustomUser
        fields = ['nome', 'email', 'idade', 'sexo', 'data_nascimento', 'password1', 'password2']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
            'idade': forms.NumberInput(attrs={'placeholder': 'Digite sua idade'}),
            'sexo': forms.Select(attrs={'placeholder': 'Selecione seu sexo'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        }
