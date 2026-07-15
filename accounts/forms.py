from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "role",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
            "password1": "Password",
            "password2": "Confirm Password",
        }

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        for name, placeholder in placeholders.items():
            self.fields[name].widget.attrs["placeholder"] = placeholder


class EmailAuthenticationForm(AuthenticationForm):

    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email",
                "class": "form-control",
            }
        ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your password",
                "class": "form-control",
            }
        )
    )
