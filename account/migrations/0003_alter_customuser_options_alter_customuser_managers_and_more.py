# Generated by Django 4.1 on 2024-01-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_remove_customuser_username"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={},
        ),
        migrations.AlterModelManagers(
            name="customuser",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="is_staff",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                error_messages={
                    "unique": "A user is already registered with this email address"
                },
                max_length=254,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.PositiveSmallIntegerField(
                blank=True, choices=[(2, "USER"), (1, "ADMIN")], default=2
            ),
        ),
    ]
