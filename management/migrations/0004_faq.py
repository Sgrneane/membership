# Generated by Django 4.1 on 2024-02-11 07:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0003_membership_associated_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="FAQ",
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
                ("question", models.TextField()),
                ("answer", models.TextField()),
            ],
        ),
    ]
