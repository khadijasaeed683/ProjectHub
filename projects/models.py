from django.conf import settings
from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Task(models.Model):

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("progress", "In Progress"),
        ("done", "Done"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="todo"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title