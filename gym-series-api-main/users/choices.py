from django.db import models


class UserTypeChoice(models.TextChoices):
    STUDENT = "STU", "Student"
    TEACHER = "TEA", "Teacher"
