from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail



class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )
    first_name = forms.CharField(
        label="Имя",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите имя"}
        ),
    )
    last_name = forms.CharField(
        label="Фамилия",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите фамилию"}
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]
        labels = {
            "username": "Имя пользователя",
            "email": "Email",
            "password1": "Пароль",
            "password2": "Подтверждение пароля",
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"\
        

class SupportForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email"}
        ),
    )
    subject = forms.CharField(
        label="Subject",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter subject"}
        ),
    )
    message = forms.CharField(
        label="Message",
        required=True,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Write your problem"}
        ),
    )

    class Meta:
        fields = ["email", "message"]

    def __init__(self, *args, **kwargs):
        super(SupportForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["message"].widget.attrs["class"] = "form-control"\
