from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    # Display columns on the Users list page
    list_display = (
        "email",
        "role",
        "is_staff",
        "is_superuser",
        "is_active",
        "last_login",
    )

    # Filters in the right sidebar
    list_filter = (
        "role",
        "is_staff",
        "is_superuser",
        "is_active",
    )

    # Search bar
    search_fields = (
        "email",
    )

    ordering = (
        "email",
    )

    # Sections shown when editing an existing user
    fieldsets = (
        (
            "Authentication",
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),

        (
            "Personal Information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "role",
                )
            },
        ),

        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),

        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )

    # Fields shown when creating a new user in Admin
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "role",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                ),
            },
        ),
    )