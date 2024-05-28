from rest_framework import serializers
from users.validators import validator_email, validator_username, validator_password
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50, validators=[validator_username])
    email = serializers.CharField(max_length=100, validators=[validator_email])
    password = serializers.CharField(max_length=250, validators=[validator_password])
    type = serializers.ChoiceField(choices=["Teacher", "Student"], required=False)
    full_name = serializers.CharField(max_length=150)


class UserConfirmationRequestEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)


class UserConfirmationRequestCodeSerializer(serializers.Serializer):
    code = serializers.CharField(write_only=True)
