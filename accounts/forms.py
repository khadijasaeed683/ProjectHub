from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

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


from django.contrib.auth.forms import AuthenticationForm

class EmailAuthenticationForm(AuthenticationForm):

    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "placeholder": "Enter your email"
        })
    )