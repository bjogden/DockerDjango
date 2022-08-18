from django.test import TestCase
from rest_framework.test import APIClient

from .models import User


class UserViewTestCase(TestCase):
    API = "/api/users/"

    def setUp(self) -> None:
        self.request = APIClient()

        User.objects.bulk_create(
            [
                User(email="foo@bar.com"),
                User(email="yee@haw.com"),
            ]
        )

    def test_get_users(self):
        response = self.request.get(self.API, format="json")
        self.assertEqual(200, response.status_code)
        output = response.data
        self.assertEqual(2, output["count"])
        self.assertEqual(2, len(output["results"]))
