from django.db import models
from django.contrib.auth.models import AbstractUser
from users.choices import UserTypeChoice


class User(AbstractUser):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    bithdate = models.DateField(null=True)
    picture = models.CharField(max_length=255)
    type = models.CharField(
        max_length=15, choices=UserTypeChoice.choices, default=UserTypeChoice.STUDENT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        return f"{self.id} - {self.username}"


class UserConfirmation(models.Model):
    code = models.CharField(max_length=6)
    is_confirmed = models.BooleanField(default=False)
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name="user_confirmation"
    )

    class Meta:
        verbose_name = "user Confirmation"
        verbose_name_plural = "users Confirmation"

    def __str__(self) -> str:
        return f"{self.id} - {self.code} - {self.user.full_name}"
