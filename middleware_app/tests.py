import os

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from middleware.redis_client import redis_client


class MiddlewareTests(TestCase):

    def setUp(self):
        redis_client.flushdb()

        self.user = User.objects.create_user(
            email="gold@test.com",
            password="password123",
            role="gold",
        )

    def tearDown(self):
        redis_client.flushdb()

    def test_logging_middleware(self):

        self.client.get(reverse("home"))

        logfile = os.path.join(
            settings.BASE_DIR,
            "logs",
            "request.log",
        )

        self.assertTrue(os.path.exists(logfile))

    def test_dashboard_redirect(self):

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 302)

    def test_gold_user_access(self):

        self.client.login(
            username="gold@test.com",
            password="password123",
        )

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
