# Generated by Django 4.2.5 on 2023-09-29 21:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_userconfirmation"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userconfirmation",
            options={
                "verbose_name": "user Confirmation",
                "verbose_name_plural": "users Confirmation",
            },
        ),
    ]
