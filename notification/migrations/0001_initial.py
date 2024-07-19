# Generated by Django 4.1 on 2024-02-06 06:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Groups",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=2000)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "users",
                    models.ManyToManyField(
                        related_name="notification_groups", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notifications",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("subject", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=2000)),
                ("status", models.BooleanField()),
                (
                    "groups",
                    models.ManyToManyField(
                        related_name="groups", to="notification.groups"
                    ),
                ),
            ],
        ),
    ]