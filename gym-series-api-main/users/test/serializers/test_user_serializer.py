from django.test import TestCase
from users.serializers import UserCreateSerializer


class UserCreateSerializerTestCase(TestCase):
    def test_user_serializer_valid(self):
        data = {
            "username": "test",
            "email": "test@test.com",
            "full_name": "Test 123",
            "password": "@Test123",
        }

        serializer = UserCreateSerializer(data=data)

        self.assertTrue(serializer.is_valid())

    def test_user_serializer_invalid(self):
        data = {
            "full_name": "Test 123",
            "password": "@test123",
        }

        serializer = UserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors["username"][0].code, "required")
        self.assertEqual(
            serializer.errors["username"][0].title(), "This Field Is Required."
        )
        self.assertEqual(serializer.errors["email"][0].code, "required")
        self.assertEqual(
            serializer.errors["email"][0].title(), "This Field Is Required."
        )

    def test_user_serializer_username_invalid(self):
        data = {
            "username": "tt",
            "email": "test@test.com",
            "full_name": "Test 123",
            "password": "@test123",
        }

        serializer = UserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors["username"][0].title(),
            "Username Precisa Ter Pelo Menos 4 Caracteres",
        )

    def test_user_serializer_email_invalid(self):
        data = {
            "username": "test",
            "email": "test",
            "full_name": "Test 123",
            "password": "@test123",
        }

        serializer = UserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors["email"][0].title(),
            "O E-Mail Não Está Em Um Formato Válido",
        )

    def test_user_serializer_password_invalid(self):
        data = {
            "username": "test",
            "email": "test@test.com",
            "full_name": "Test 123",
            "password": "Test123",
        }

        serializer = UserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors["password"][0].title(),
            "A Senha Deve Ter Pelo Menos Caractere Especial.",
        )
