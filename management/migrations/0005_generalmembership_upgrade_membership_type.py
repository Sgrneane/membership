# Generated by Django 4.1 on 2024-02-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0004_faq"),
    ]

    operations = [
        migrations.AddField(
            model_name="generalmembership",
            name="upgrade_membership_type",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "General"),
                    (2, "Institutional"),
                    (3, "Lifetime"),
                    (4, "Student"),
                ],
                null=True,
            ),
        ),
    ]
