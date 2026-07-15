from django.test import TestCase
from django.urls import reverse

from accounts.models import User


class ProjectViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com",
            password="password123",
            first_name="Khadija",
            role="gold",
        )

    def test_home_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 302)

    def test_dashboard_authenticated(self):
        self.client.login(username="test@test.com", password="password123")

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
