from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class User(AbstractUser):
    ROLE_CHOICES = [
        ("gold", "Gold"),
        ("silver", "Silver"),
        ("bronze", "Bronze"),
    ]

    username = None

    email = models.EmailField(unique=True)

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="bronze")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Create your models here.
