from django.test import TestCase
from rest_framework import exceptions

from users.models import User
from users.services import UserService


class UserServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.service = UserService()

    def test_create_user(self):
        payload = {
            "full_name": "Teste case",
            "email": "test@gmail.com",
            "password": "@1T2este",
            "username": "teste123",
        }

        user = self.service.create_user(payload)

        self.assertIsInstance(user, User)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(email=payload.get("email")).exists())

    def test_create_user_exception_already_user(self):
        User.objects.create(username="teste123", email="test@gmail.com")
        payload = {
            "full_name": "Teste case",
            "email": "test@gmail.com",
            "password": "@1T2este",
            "username": "teste123",
        }
        with self.assertRaises(exceptions.APIException) as ctx:
            self.service.create_user(payload)

        self.assertEqual(
            ctx.exception.detail.title(),
            "Já Existe Um Usuário Com Esse Username/Email.",
        )
