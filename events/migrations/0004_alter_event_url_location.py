# Generated by Django 4.1 on 2024-02-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0003_alter_event_url_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="url_location",
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
