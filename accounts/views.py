from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import (
    UserRegistrationForm,
    EmailAuthenticationForm,
)


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class CustomLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = "registration/login.html"


class CustomLogoutView(LogoutView):
    template_name = "registration/logged_out.html"