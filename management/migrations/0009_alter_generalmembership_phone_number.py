# Generated by Django 4.1 on 2024-07-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0008_alter_generalmembership_salutation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generalmembership",
            name="phone_number",
            field=models.CharField(max_length=20, null=True),
        ),
    ]