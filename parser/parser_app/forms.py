from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterUserFrom(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )
